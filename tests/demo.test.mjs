import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
await import('../docs/assets/demo-data.js');
const demo=globalThis.NovelDemo;
test('four scene demo has a real 36 second duration',()=>{
  assert.equal(demo.duration,36);assert.equal(demo.scenes.length,4);
  assert.equal(demo.scenes.reduce((sum,x)=>sum+x.duration,0),36);
});
test('each scene is available in both languages with readable copy',()=>{
  for(const scene of demo.scenes)for(const lang of ['zh','en']){
    const text=scene[lang];assert.ok(text.title);assert.ok(text.summary);assert.ok(text.label);
  }
});
test('timeline chooses exact scene boundaries',()=>{
  assert.equal(demo.sceneAt(0),0);assert.equal(demo.sceneAt(8.99),0);
  assert.equal(demo.sceneAt(9),1);assert.equal(demo.sceneAt(18),2);
  assert.equal(demo.sceneAt(27),3);assert.equal(demo.sceneAt(36),3);
});
test('timeline rejects unsafe values by clamping',()=>{
  for(const value of [NaN,Infinity,-10])assert.equal(demo.normalizeTime(value),0);
  assert.equal(demo.normalizeTime(99),36);
});
test('demo is explicitly illustrative, not a recorded model response',()=>{
  assert.equal(demo.illustrative,true);assert.match(demo.disclaimer.zh,/示意/);assert.match(demo.disclaimer.en,/illustrative/i);
});
test('entry still describes the actual installation and author confirmation',()=>{
  assert.match(demo.installCommand,/npx skills/);
  assert.match(demo.scenes[2].zh.title,/作者/);
});
test('canonical player has no third-party runtime requests',()=>{
  const html=fs.readFileSync(new URL('../docs/demo.html',import.meta.url),'utf8');
  assert.doesNotMatch(html,/<script[^>]+src=["']https?:/i);
  assert.doesNotMatch(html,/<link[^>]+href=["']https?:/i);
  assert.match(html,/demo-player\.js/);assert.match(html,/demo\.css/);
});
test('page video is user-controlled and does not preload the full MP4',()=>{
  const html=fs.readFileSync(new URL('../docs/demo.html',import.meta.url),'utf8');
  assert.match(html,/<video[^>]+controls/);assert.match(html,/preload="none"/);
  assert.doesNotMatch(html,/<video[^>]+autoplay/);
});
test('motion preferences, keyboard focus and timing controls are provided',()=>{
  const css=fs.readFileSync(new URL('../docs/assets/demo.css',import.meta.url),'utf8');
  const html=fs.readFileSync(new URL('../docs/demo.html',import.meta.url),'utf8');
  assert.match(css,/prefers-reduced-motion/);assert.match(css,/:focus-visible/);
  assert.match(html,/aria-label="Timeline"/);assert.match(html,/id="play-toggle"/);
});
test('both READMEs link to the hosted player, not HTML source',()=>{
  for(const name of ['README.md','README.en.md']){
    const text=fs.readFileSync(new URL('../'+name,import.meta.url),'utf8');
    assert.match(text,/https:\/\/huo0077\.github\.io\/novel-writing-skills\/demo\.html/i);
    assert.doesNotMatch(text,/\]\(docs\/demo\.html\)/);
    assert.doesNotMatch(text,/70秒|70 秒|70s Showcase|1080P/);
  }
});

function playerHarness(){
  const elements=new Map();
  function element(id){
    if(!elements.has(id))elements.set(id,{value:'0',readyState:0,dataset:{},listeners:{},addEventListener(name,fn){this.listeners[name]=fn;},querySelectorAll(){return [];},setAttribute(){},load(){}});
    return elements.get(id);
  }
  const context={URLSearchParams,location:{search:''},performance:{now:()=>0},requestAnimationFrame(){},document:{documentElement:{dataset:{}},hidden:false,getElementById:element,addEventListener(){}}};
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(new URL('../docs/assets/demo-data.js',import.meta.url),'utf8'),context);
  vm.runInContext(fs.readFileSync(new URL('../docs/assets/demo-player.js',import.meta.url),'utf8'),context);
  return {context,element};
}
test('scrubbing reads the requested value before pause renders the old position',()=>{
  const h=playerHarness();const timeline=h.element('timeline');timeline.value='27';timeline.listeners.input({target:timeline});
  assert.equal(h.context.NovelDemoPlayer.getState().time,27);assert.equal(h.context.NovelDemoPlayer.getState().scene,3);
});
test('previous chapter works after a scrub to the last scene',()=>{
  const h=playerHarness();const timeline=h.element('timeline');timeline.value='27';timeline.listeners.input({target:timeline});
  h.element('previous').listeners.click();assert.equal(h.context.NovelDemoPlayer.getState().scene,2);
});

test('preview assets match the declared dimensions and saved byte sizes',()=>{
  const manifest=JSON.parse(fs.readFileSync(new URL('../docs/assets/demo-media.json',import.meta.url),'utf8'));
  assert.equal(manifest.interactive_seconds,36);assert.equal(manifest.gif_preview_seconds,12);assert.equal(manifest.illustrative,true);
  for(const item of manifest.exports){
    const gif=fs.readFileSync(new URL('../docs/assets/'+item.gif.file,import.meta.url));
    assert.equal(gif.length,item.gif.bytes);assert.equal(gif.readUInt16LE(6),960);assert.equal(gif.readUInt16LE(8),540);
    const mp4=fs.readFileSync(new URL('../docs/assets/'+item.mp4.file,import.meta.url));assert.equal(mp4.length,item.mp4.bytes);
  }
});
test('both MP4 exports use H.264 and put the metadata before media payload',()=>{
  for(const name of ['novel-skills-demo-36s.mp4','novel-skills-demo-36s.en.mp4']){
    const file=fs.readFileSync(new URL('../docs/assets/'+name,import.meta.url));assert.ok(file.includes(Buffer.from('avc1')));
    const atoms=[];for(let offset=0;offset+8<=file.length;){const size=file.readUInt32BE(offset);if(size<8)break;atoms.push(file.toString('ascii',offset+4,offset+8));offset+=size;}
    assert.ok(atoms.indexOf('moov')>=0);assert.ok(atoms.indexOf('moov')<atoms.indexOf('mdat'));
  }
});
