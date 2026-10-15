/* Local, deterministic presentation data. No model/network calls. */
(() => {
  const scenes = [
    {id:'overview',duration:9,
      zh:{label:'01 / 写作痛点',title:'长篇写作，不只需要流畅。',summary:'让人物状态、伏笔与每一次修改，都有据可查。'},
      en:{label:'01 / THE PROBLEM',title:'A novel needs more than fluent prose.',summary:'Keep character state, clues, and revisions traceable.'}},
    {id:'review',duration:9,
      zh:{label:'02 / 找到依据',title:'先核对事实，再修改表达。',summary:'伤势、物品、知识边界：把正文与已有记录放在一起。'},
      en:{label:'02 / FIND THE EVIDENCE',title:'Check the facts before polishing.',summary:'Compare the draft with injuries, possessions, and knowledge records.'}},
    {id:'ask',duration:9,
      zh:{label:'03 / 作者决定',title:'资料不足，让作者来决定。',summary:'提供有差异的方向，而不是把猜测写成正史。'},
      en:{label:'03 / THE AUTHOR DECIDES',title:'Missing a fact? Ask the author.',summary:'Offer meaningful options instead of turning guesses into canon.'}},
    {id:'result',duration:9,
      zh:{label:'04 / 回审与恢复',title:'改写可回审，进度可恢复。',summary:'草稿不自动成为正史；下一步只推进已获准的范围。'},
      en:{label:'04 / REVIEW AND RESUME',title:'Review the change. Save the next step.',summary:'A draft is not canon. Continue only within the approved scope.'}}
  ];
  const duration=scenes.reduce((sum,s)=>sum+s.duration,0);
  const normalizeTime=value=>Number.isFinite(value)?Math.min(duration,Math.max(0,value)):0;
  const sceneAt=value=>Math.min(scenes.length-1,Math.floor(normalizeTime(value)/9));
  globalThis.NovelDemo=Object.freeze({duration,scenes,sceneAt,normalizeTime,illustrative:true,
    disclaimer:{zh:'流程示意 · 非模型实录 · 不保证自动发现全部问题',en:'Illustrative workflow · Not a live model recording · Not an exhaustive audit'},
    installCommand:'npx skills add Huo0077/novel-writing-skills'});
})();
