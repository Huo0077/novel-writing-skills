#!/usr/bin/env node
/** Initialize project records from the installed router, without Python or dependencies.
 * No network, automatic postinstall, source mutation, overwriting or deletion.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const DEFAULT_ROUTER = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const NAME = /^novel-[a-z0-9-]+$/;
function inside(child, parent) {
  const rel = path.relative(parent, child);
  return rel === '' || (rel !== '..' && !rel.startsWith('..' + path.sep) && !path.isAbsolute(rel));
}
function assertUnlinkedDestination(target) {
  let cursor = path.resolve(target);
  while (true) {
    try {
      if (fs.lstatSync(cursor).isSymbolicLink()) throw new Error('Linked destination is not permitted: ' + cursor);
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
    }
    const parent = path.dirname(cursor);
    if (parent === cursor) break;
    cursor = parent;
  }
}
function seedFiles(seed) {
  const files = [];
  function walk(directory) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true }).sort((a,b)=>a.name.localeCompare(b.name))) {
      const full = path.join(directory, entry.name);
      if (entry.isSymbolicLink()) throw new Error('Linked seed resource is not permitted: ' + full);
      if (entry.isDirectory()) walk(full);
      else if (entry.isFile()) files.push({source: full, relative: path.relative(seed, full).split(path.sep).join('/')});
      else throw new Error('Unsupported seed entry: ' + full);
    }
  }
  walk(seed);
  return files;
}
export function inspectInstallation(routerPath = DEFAULT_ROUTER) {
  const router = path.resolve(routerPath);
  const report = {mode:'check',routerPath:router,skillsRoot:path.dirname(router),seedRoot:path.join(router,'assets','project-seed','.novel'),catalogVersion:null,skillCount:0,missingSkills:[],errors:[]};
  try {
    const data = JSON.parse(fs.readFileSync(path.join(router,'references','catalog.json'),'utf8').replace(/^\uFEFF/,''));
    if (!Array.isArray(data.skills) || !data.skills.length) throw new Error('Catalog skills must be a nonempty list');
    const names = data.skills.map(item=>item?.name);
    if (names.some(name=>typeof name!=='string'||!NAME.test(name)) || new Set(names).size!==names.length || !names.includes('novel-router')) throw new Error('Invalid or duplicate catalog skill names');
    report.catalogVersion=data.version;report.skillCount=names.length;
    for (const name of names) {
      if (!fs.existsSync(path.join(report.skillsRoot,name,'SKILL.md'))) report.missingSkills.push(name);
    }
    if (report.missingSkills.length) report.errors.push('Incomplete skill installation; install the complete suite: '+report.missingSkills.join(', '));
    if (!fs.statSync(report.seedRoot).isDirectory() || !fs.statSync(path.join(report.seedRoot,'project.yaml')).isFile()) throw new Error('Missing clean project seed/project.yaml');
    seedFiles(report.seedRoot);
  } catch(error) {
    report.errors.push('Installation resource error: '+error.message);
  }
  report.limits=['resource_and_presence_check_not_semantic_validation','no_python_or_network_required','no_author_decisions_created'];
  return report;
}
export function initializeProject({routerPath=DEFAULT_ROUTER,target=process.cwd(),apply=false} = {}) {
  const installation=inspectInstallation(routerPath);
  if (installation.errors.length) throw new Error('Installation is incomplete: '+installation.errors.join('; '));
  const project=path.resolve(target);
  assertUnlinkedDestination(project);
  if (inside(project,installation.skillsRoot)) throw new Error('Project target must not be inside the installed skill collection');
  if (fs.existsSync(project) && !fs.statSync(project).isDirectory()) throw new Error('Project target is not a directory');
  const files=seedFiles(installation.seedRoot);
  const report={mode:apply?'apply':'preview',target:project,routerPath:installation.routerPath,skillCount:installation.skillCount,catalogVersion:installation.catalogVersion,create:[],preserve:[],warnings:[]};
  // Preflight all paths before creating anything, including conflicting parent files.
  for (const item of files) {
    const rel='.novel/'+item.relative;
    const dest=path.resolve(project,'.novel',...item.relative.split('/'));
    if (!inside(dest,path.join(project,'.novel'))) throw new Error('Seed path escapes project directory');
    assertUnlinkedDestination(dest);
    if (fs.existsSync(dest)) {
      if (!fs.statSync(dest).isFile()) throw new Error('File destination is a directory: '+dest);
      report.preserve.push(rel);
    } else {
      for (let parent=path.dirname(dest); ;parent=path.dirname(parent)) {
        if (fs.existsSync(parent) && !fs.statSync(parent).isDirectory()) throw new Error('Destination parent is not a directory: '+parent);
        if (path.dirname(parent)===parent) break;
      }
      report.create.push(rel);
    }
  }
  if (apply) {
    for (const rel of report.create) {
      const relative=rel.slice('.novel/'.length);
      const source=path.join(installation.seedRoot,...relative.split('/'));
      const dest=path.join(project,...rel.split('/'));
      assertUnlinkedDestination(dest);
      fs.mkdirSync(path.dirname(dest),{recursive:true});
      // Exclusive write prevents truncation if another writer created a file meanwhile.
      fs.writeFileSync(dest,fs.readFileSync(source),{flag:'wx'});
    }
  }
  if (report.preserve.length) report.warnings.push('Existing files were preserved, not merged or approved; review old schema compatibility.');
  report.nextStep='Ask the creator one blocking question with options; do not invent story facts.';
  report.limits=['not_transactional_against_concurrent_directory_changes','no_story_facts_approved','no_skills_removed_or_reinstalled'];
  return report;
}
export function main(argv=process.argv.slice(2),io={write:s=>process.stdout.write(s),error:s=>process.stderr.write(s)}) {
  try {
    let routerPath=DEFAULT_ROUTER,target=process.cwd(),apply=false,check=false;
    if (argv.includes('--help')||argv.includes('-h')) {
      io.write('Usage: node init-project.mjs [--target PATH] [--apply | --check]\nDefault: preview only. --apply adds missing .novel files, preserving existing files.\n--check validates installed resources without creating a project. --router PATH is an explicit relocated-source override.\n');return 0;
    }
    for(let i=0;i<argv.length;i++) {
      const arg=argv[i];
      if(arg==='--apply')apply=true;
      else if(arg==='--check')check=true;
      else if(arg==='--target'||arg==='--router') {
        const value=argv[++i];if(!value||value.startsWith('--'))throw new Error('Missing value for '+arg);
        if(arg==='--target')target=value;else routerPath=value;
      } else throw new Error('Unknown argument: '+arg);
    }
    if(apply&&check)throw new Error('--check and --apply are mutually exclusive');
    const report=check?inspectInstallation(routerPath):initializeProject({routerPath,target,apply});
    io.write(JSON.stringify(report,null,2)+'\n');
    return report.errors?.length?1:0;
  } catch(error) {io.error('ERROR: '+error.message+'\n');return 2;}
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url))process.exitCode=main();
