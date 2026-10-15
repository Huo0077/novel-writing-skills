import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { inspectInstallation, initializeProject, main } from '../scripts/init-project.mjs';

const script = fileURLToPath(new URL('../scripts/init-project.mjs', import.meta.url));
function setup(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'novel-node-test-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const skills = path.join(root, 'installed', '.agents', 'skills');
  const router = path.join(skills, 'novel-router');
  const seed = path.join(router, 'assets', 'project-seed', '.novel');
  fs.mkdirSync(path.join(router, 'references'), { recursive: true });
  fs.mkdirSync(path.join(skills, 'novel-world'), { recursive: true });
  fs.writeFileSync(path.join(router, 'SKILL.md'), 'router');
  fs.writeFileSync(path.join(skills, 'novel-world', 'SKILL.md'), 'world');
  fs.writeFileSync(path.join(router, 'references', 'catalog.json'), JSON.stringify({version:'1.2',skills:[{name:'novel-router'},{name:'novel-world'}]}));
  fs.mkdirSync(path.join(seed, 'schemas'), { recursive: true });
  fs.mkdirSync(path.join(seed, 'drafts', 'chapters'), { recursive: true });
  fs.writeFileSync(path.join(seed, 'project.yaml'), 'title: "未命名小说"\n');
  fs.writeFileSync(path.join(seed, 'schemas', 'test.md'), 'protocol');
  fs.writeFileSync(path.join(seed, 'drafts', 'chapters', '.keep'), '');
  return {root,skills,router,seed,target:path.join(root,'作品目录')};
}
test('inspects resources relative to the installed router, not cwd',t=>{
  const x=setup(t),r=inspectInstallation(x.router);
  assert.deepEqual(r.errors,[]);assert.equal(r.skillCount,2);assert.equal(r.skillsRoot,x.skills);
});
test('preview does not create a target directory',t=>{
  const x=setup(t),r=initializeProject({routerPath:x.router,target:x.target});
  assert.equal(r.mode,'preview');assert.equal(fs.existsSync(x.target),false);assert.ok(r.create.includes('.novel/project.yaml'));
});
test('apply creates clean project records only, never another skill installation',t=>{
  const x=setup(t);const r=initializeProject({routerPath:x.router,target:x.target,apply:true});
  assert.equal(r.mode,'apply');assert.ok(fs.existsSync(path.join(x.target,'.novel','project.yaml')));
  assert.equal(fs.existsSync(path.join(x.target,'.agents')),false);assert.equal(fs.existsSync(path.join(x.target,'.codex')),false);
});
test('existing creator file is preserved byte for byte',t=>{
  const x=setup(t);fs.mkdirSync(path.join(x.target,'.novel'),{recursive:true});
  const p=path.join(x.target,'.novel','project.yaml');const bytes=Buffer.from('title: 我的小说\n');fs.writeFileSync(p,bytes);
  const r=initializeProject({routerPath:x.router,target:x.target,apply:true});
  assert.ok(r.preserve.includes('.novel/project.yaml'));assert.deepEqual(fs.readFileSync(p),bytes);
});
test('a second application creates zero files',t=>{
  const x=setup(t);initializeProject({routerPath:x.router,target:x.target,apply:true});
  assert.deepEqual(initializeProject({routerPath:x.router,target:x.target,apply:true}).create,[]);
});
test('global installation source initializes only explicitly selected project',t=>{
  const x=setup(t);const sourceBefore=fs.readdirSync(path.join(x.router,'assets','project-seed','.novel'));
  initializeProject({routerPath:x.router,target:x.target,apply:true});
  assert.deepEqual(fs.readdirSync(path.join(x.router,'assets','project-seed','.novel')),sourceBefore);
  assert.equal(fs.existsSync(path.join(x.skills,'.novel')),false);
});
test('missing sibling skill is reported and prevents writing',t=>{
  const x=setup(t);fs.rmSync(path.join(x.skills,'novel-world'),{recursive:true});
  assert.ok(inspectInstallation(x.router).errors.some(s=>s.includes('novel-world')));
  assert.throws(()=>initializeProject({routerPath:x.router,target:x.target,apply:true}),/installation/i);
  assert.equal(fs.existsSync(x.target),false);
});
test('missing seed is reported before writing',t=>{
  const x=setup(t);fs.rmSync(x.seed,{recursive:true});
  assert.ok(inspectInstallation(x.router).errors.length);assert.throws(()=>initializeProject({routerPath:x.router,target:x.target,apply:true}));
  assert.equal(fs.existsSync(x.target),false);
});
test('missing seed project descriptor is reported',t=>{
  const x=setup(t);fs.unlinkSync(path.join(x.seed,'project.yaml'));assert.ok(inspectInstallation(x.router).errors.length);
});
test('malformed catalog is rejected',t=>{
  const x=setup(t);fs.writeFileSync(path.join(x.router,'references','catalog.json'),'{bad');assert.ok(inspectInstallation(x.router).errors.length);
});
test('catalog traversal name is rejected',t=>{
  const x=setup(t);fs.writeFileSync(path.join(x.router,'references','catalog.json'),JSON.stringify({version:'1.2',skills:[{name:'../escape'}]}));
  assert.ok(inspectInstallation(x.router).errors.length);
});
test('duplicate catalog names are rejected',t=>{
  const x=setup(t);fs.writeFileSync(path.join(x.router,'references','catalog.json'),JSON.stringify({version:'1.2',skills:[{name:'novel-router'},{name:'novel-router'}]}));
  assert.ok(inspectInstallation(x.router).errors.length);
});
test('directory occupying a file destination causes no partial writes',t=>{
  const x=setup(t);fs.mkdirSync(path.join(x.target,'.novel','schemas','test.md'),{recursive:true});
  assert.throws(()=>initializeProject({routerPath:x.router,target:x.target,apply:true}),/directory|file/i);
  assert.equal(fs.existsSync(path.join(x.target,'.novel','project.yaml')),false);
});
test('file occupying a destination parent causes no writes',t=>{
  const x=setup(t);fs.mkdirSync(x.target);fs.writeFileSync(path.join(x.target,'.novel'),'not a directory');
  assert.throws(()=>initializeProject({routerPath:x.router,target:x.target,apply:true}),/directory|file/i);
});
test('initializing inside installed skills is rejected',t=>{
  const x=setup(t);assert.throws(()=>initializeProject({routerPath:x.router,target:path.join(x.router,'bad'),apply:true}),/skill/i);
});
test('existing unrelated manuscripts are untouched',t=>{
  const x=setup(t);fs.mkdirSync(x.target);const p=path.join(x.target,'my-chapter.txt');fs.writeFileSync(p,'原稿');
  initializeProject({routerPath:x.router,target:x.target,apply:true});assert.equal(fs.readFileSync(p,'utf8'),'原稿');
});
test('symlinked target is rejected when OS permits creating it',t=>{
  const x=setup(t);const actual=path.join(x.root,'actual');fs.mkdirSync(actual);
  try{fs.symlinkSync(actual,x.target,'junction');}catch(e){t.skip('symlink/junction permission unavailable');return;}
  assert.throws(()=>initializeProject({routerPath:x.router,target:x.target,apply:true}),/link/i);
});
test('project remains after installed skills are removed in isolation',t=>{
  const x=setup(t);initializeProject({routerPath:x.router,target:x.target,apply:true});
  fs.rmSync(path.join(x.root,'installed'),{recursive:true});assert.ok(fs.existsSync(path.join(x.target,'.novel','project.yaml')));
});
test('main check works with an explicit router source and never initializes',t=>{
  const x=setup(t);let output='';const code=main(['--check','--router',x.router,'--target',x.target],{write:s=>output+=s,error:()=>{}});
  assert.equal(code,0);assert.equal(JSON.parse(output).mode,'check');assert.equal(fs.existsSync(x.target),false);
});
test('main accepts preview/apply with an explicit target',t=>{
  const x=setup(t);let output='';const code=main(['--router',x.router,'--target',x.target,'--apply'],{write:s=>output+=s,error:()=>{}});
  assert.equal(code,0);assert.equal(JSON.parse(output).mode,'apply');
});
test('unknown arguments and conflicting flags return error',()=>{
  for(const args of [['--wat'],['--target'],['--check','--apply']]){
    assert.equal(main(args,{write:()=>{},error:()=>{}}),2);
  }
});
test('help does not require a project or Python',()=>{
  let text='';assert.equal(main(['--help'],{write:s=>text+=s,error:()=>{}}),0);assert.match(text,/--target/);
});
test('CLI runs without Python or a third-party Node dependency',()=>{
  const result=spawnSync(process.execPath,[script,'--help'],{encoding:'utf8',env:{...process.env,PATH:path.dirname(process.execPath)}});
  assert.equal(result.status,0);assert.match(result.stdout,/--apply/);
});
