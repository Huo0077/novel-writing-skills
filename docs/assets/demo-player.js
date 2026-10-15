(() => {
'use strict';
const model=globalThis.NovelDemo;
const params=new URLSearchParams(location.search);
let lang=params.get('lang')==='en'?'en':'zh';
let current=0,playing=false,lastStamp=0,currentScene=-1;
const $=id=>document.getElementById(id);
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=time=>`00:${String(Math.floor(time)).padStart(2,'0')}`;
const pick=(zh,en)=>lang==='zh'?zh:en;
const panel=(label,body)=>`<div class="panel"><div class="panel-label">${label}</div>${body}</div>`;
function content(index){
 const scene=model.scenes[index][lang];
 let body='';
 if(index===0){
  const cards=lang==='zh'?[['状态不断线','伤势、物品、认知，先读已有依据。'],['表达不磨平','找出无效重复，也保留主题回环。'],['决定不越界','缺信息先问，重大改变先确认。']]:[['Keep state consistent','Check injuries, possessions, and knowledge against records.'],['Preserve your voice','Reduce empty repetition, not intentional motifs.'],['Keep the author in control','Ask about gaps. Confirm consequential changes.']];
  body=`<div class="three-columns">${cards.map((c,i)=>`<div class="panel"><span class="number">0${i+1}</span><h2>${c[0]}</h2><p>${c[1]}</p><div class="mini-rule"></div></div>`).join('')}</div><p class="two-line-note">${pick('不是一次性写完一本书，而是让每一场都能接上前文。','Not a one-click novel. A workflow that connects each scene to what came before.')}</p>`;
 }else if(index===1){
  const quote=pick('他<span class="issue">挥起右手</span>，从衣袋<span class="issue">取出钥匙</span>。这一刻，他忽然<span class="issue">明白了她的身世</span>。','He <span class="issue">raised his right hand</span> and <span class="issue">took out the key</span>. Suddenly, he <span class="issue">understood her hidden past</span>.');
  const rows=lang==='zh'?[['右腕仍有夹板','依据：前一场身体状态。'],['钥匙已交给何青','依据：物品转移记录。'],['身世没有获知来源','不能把作者答案写进角色脑中。']]:[['His wrist is still splinted','Source: the previous scene’s physical state.'],['He Qing holds the key','Source: the recorded transfer.'],['No source for that knowledge','Author truth is not character knowledge.']];
  body=`<div class="split">${panel(pick('问题草稿 / DRAFT','A PROBLEM DRAFT'),`<p class="draft-text">${quote}</p>`)}${panel(pick('与已有记录对照','CHECK AGAINST RECORDS'),`<div class="evidence-list">${rows.map((c,i)=>`<div class="evidence"><span class="evidence-index">${i+1}</span><div><strong>${c[0]}</strong><small>${c[1]}</small></div></div>`).join('')}</div>`)}</div>`;
 }else if(index===2){
  const options=lang==='zh'?['保留旧记录，由何青开门。','补充钥匙归还的时点与依据。','本场先停在门外，只核查路线。']:['Keep the record: He Qing opens the door.','Confirm when and how the key was returned.','Stay outside and check the route first.'];
  body=`<div class="split">${panel(pick('一个当前关键问题','ONE BLOCKING QUESTION'),`<p class="question">${pick('这次开门，如何衔接钥匙记录？','How should opening the door fit the key record?')}</p><div class="options">${options.map((c,i)=>`<div class="option"><span class="option-key">${'ABC'[i]}</span><p>${c}</p></div>`).join('')}</div><div class="author-note">${pick('演示中的作者答复：选 C。也可自定义或暂缓。','Illustrative author response: C. Custom answers or deferral are also valid.')}</div>`)}<div class="author-side"><h2>${pick('推荐 ≠ 选择<br>草稿 ≠ 正史','A suggestion is not a decision.<br>A draft is not canon.')}</h2><p>${pick('只确认回答的范围。<br>“留在门外”不等于批准归还钥匙、进入仓库或揭示身份。','An answer approves only its stated scope. Staying outside does not approve a key transfer, entry, or an identity reveal.')}</p></div></div>`;
 }else{
  const quote=pick('他把右腕贴回身侧，看向何青手里的钥匙。<br>“先别开。”他说，“我只核对外面的路。”','He kept his injured wrist at his side and glanced at the key in He Qing’s hand.<br>“Not yet,” he said. “I’m only checking the route outside.”');
  const states=lang==='zh'?['仍未入门','钥匙仍在何青处','身份仍未知']:['Still outside','Key stays with He Qing','Identity still unknown'];
  body=`<div class="split">${panel(pick('修订候选 / 仍是 DRAFT','REVISION CANDIDATE / STILL A DRAFT'),`<p class="draft-text">${quote}</p><div class="state-tags">${states.map(s=>`<span>${s}</span>`).join('')}</div>`)}${panel(pick('回审实际发生的变化','REVIEW WHAT ACTUALLY CHANGED'),`<div class="status-list"><div class="status-row"><strong>${pick('核对新增动作与信息','Check new actions and information')}</strong><p>${pick('语言改写也可能改变事实，不能跳过回审。','Even wording changes can introduce facts.')}</p></div><div class="status-row"><strong>${pick('保留待确认项与下一步','Save pending decisions and the next step')}</strong><p>${pick('下次恢复，只读取当前相关状态。','Resume with the relevant state, not guessed history.')}</p></div></div>`)}</div><div class="install-line">${escape(model.installCommand)}</div>`;
 }
 return `<header class="scene-header"><h1>${scene.title}</h1><p class="subline">${lang==='zh'?model.scenes[index].en.title:''}</p></header><div class="scene-body">${body}</div>`;
}
function updateLabels(){
 document.documentElement.lang=lang==='zh'?'zh-CN':'en';
 document.title=pick('小说创作 Skills · 36秒流程演示','Novel Writing Skills · 36-second workflow');
 $('brand-sub').textContent=pick('小说创作技能组','Author-controlled fiction workflow');
 $('repo-link').textContent=pick('返回 GitHub ↗','Back to GitHub ↗');
 $('lang-toggle').textContent=pick('English','中文');
 $('fullscreen').textContent=pick('全屏','Fullscreen');
 $('scope-note').textContent=pick('这是可回看、可暂停的流程示意，不是模型实录或功能效果保证。默认静音，不自动播放。','A pausable, illustrative workflow—not a live model recording or a guarantee of results. Silent, with no autoplay.');
 $('video-summary').textContent=pick('播放 36 秒 MP4 视频 / 下载','Play the 36-second MP4 / download');
 $('video-download').textContent=pick('下载 MP4（1280×720，无声）','Download MP4 (1280×720, silent)');
 $('footer-note').textContent=pick('保留原始 HTML 作为创作参考；本页不依赖外部 CDN、字体或分析脚本。','The original HTML is retained as a reference. No external CDN, fonts, or analytics scripts.');
 $('source-link').textContent=pick('查看页面源码 ↗','View page source ↗');
 $('chapters').innerHTML=model.scenes.map((s,i)=>`<button type="button" data-chapter="${i}" aria-current="${i===currentScene}">${s[lang].label}</button>`).join('');
 const suffix=lang==='en'?'.en':'';
 const video=$('demo-video');const wasLoaded=video.readyState>0;
 $('video-source').src=`assets/novel-skills-demo-36s${suffix}.mp4`;
 video.poster=`assets/demo-poster${suffix}.jpg`;
 $('video-download').href=`assets/novel-skills-demo-36s${suffix}.mp4`;
 video.src=`assets/novel-skills-demo-36s${suffix}.mp4`;
 if(wasLoaded)video.load();
}
function render(force=false){
 const index=model.sceneAt(current);
 if(index!==currentScene||force){currentScene=index;$('scene-content').innerHTML=content(index);$('scene-label').textContent=model.scenes[index][lang].label;$('scene-summary').textContent=model.scenes[index][lang].summary;$('stage-disclaimer').textContent=model.disclaimer[lang];for(const b of $('chapters').querySelectorAll('button'))b.setAttribute('aria-current',String(Number(b.dataset.chapter)===index));}
 $('timeline').value=String(current);$('time-display').textContent=`${fmt(current)} / 00:36`;$('play-toggle').textContent=playing?pick('暂停','Pause'):(current>=model.duration?pick('重新播放','Replay'):pick('播放演示','Play demo'));
}
function seek(value){current=model.normalizeTime(Number(value));render();}
function pause(){playing=false;render();}
function play(){if(current>=model.duration)current=0;playing=true;lastStamp=performance.now();render();}
function frame(stamp){if(playing){current=Math.min(model.duration,current+(stamp-lastStamp)/1000);lastStamp=stamp;if(current>=model.duration)playing=false;render();}requestAnimationFrame(frame);}
$('play-toggle').addEventListener('click',()=>playing?pause():play());
$('previous').addEventListener('click',()=>{pause();seek(Math.max(0,currentScene-1)*9);});
$('next').addEventListener('click',()=>{pause();seek(Math.min(3,currentScene+1)*9);});
$('timeline').addEventListener('input',e=>{const requestedTime=Number(e.target.value);pause();seek(requestedTime);});
$('chapters').addEventListener('click',e=>{const button=e.target.closest('[data-chapter]');if(button){pause();seek(Number(button.dataset.chapter)*9);}});
$('lang-toggle').addEventListener('click',()=>{lang=lang==='zh'?'en':'zh';updateLabels();render(true);});
$('fullscreen').addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await $('demo-stage').requestFullscreen();}catch{ $('scope-note').textContent=pick('此浏览器不支持全屏，仍可在本页播放。','Fullscreen is unavailable; you can still use the player.');}});
document.addEventListener('visibilitychange',()=>{if(document.hidden)pause();});
document.addEventListener('keydown',e=>{if(e.target.matches('input,button,a,summary,video'))return;if(e.code==='Space'){e.preventDefault();playing?pause():play();}else if(e.code==='ArrowRight'){pause();seek(current+9);}else if(e.code==='ArrowLeft'){pause();seek(current-9);}});
if(params.get('render')==='1')document.documentElement.dataset.render='true';
updateLabels();seek(Number(params.get('scene')||0)*9);render(true);requestAnimationFrame(frame);
globalThis.NovelDemoPlayer={seek,play,pause,setLanguage(value){lang=value==='en'?'en':'zh';updateLabels();render(true);},getState(){return {time:current,scene:currentScene,playing,language:lang};}};
})();
