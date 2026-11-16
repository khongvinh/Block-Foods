const {chromium}=require('playwright'); const http=require('http'),fs=require('fs'),path=require('path');
const WWW='/home/user/Block-Foods/app/www';
const FAKE=`window.__docs={other:{endless:900,earned:120000,rcount:3,rsum:14,nk:"tom:1234",at:1}};
window.BF_BACKEND={kind:"firebase",init:async()=>{
  const subs=[]; const emit=()=>subs.forEach(f=>f({docs:Object.entries(window.__docs).map(([id,d])=>({id,data:()=>d}))}));
  const db={collection:()=>({limit:()=>({onSnapshot:(f)=>{subs.push(f); setTimeout(emit,50);}}),
    doc:id=>({set:async d=>{window.__docs[id]=d;emit();},delete:async()=>{delete window.__docs[id];emit();}})})};
  return {db,user:{id:async()=>"me1",me:async()=>({}),can:async()=>true,profiles:async()=>({})}};}};`;
const srv=http.createServer((q,r)=>{ let u=decodeURIComponent(q.url.split('?')[0]); if(u==='/')u='/index.html';
  if(u==='/firebase-backend.js'&&process.env.FAKE){ r.end(FAKE); return; }
  const p=path.join(WWW,u); if(!fs.existsSync(p)){r.statusCode=404;r.end();return;}
  r.setHeader('content-type',u.endsWith('.js')?'text/javascript':u.endsWith('.html')?'text/html':'image/webp'); r.end(fs.readFileSync(p)); }).listen(8765);
(async()=>{
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:390,height:844}}); const errs=[];
  p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
  await p.goto('http://localhost:8765/'); await p.waitForTimeout(800);
  const gate=await p.$eval('#gate',e=>e.classList.contains('on'));
  const acct=await p.$eval('#acct',e=>e.hidden?'(hidden)':e.textContent);
  console.log(process.env.FAKE?'FAKE':'NOCONFIG','gate',gate,'acct',acct);
  if(process.env.FAKE){
    await p.click('#acct'); await p.waitForTimeout(200); const n1=await p.textContent('#nkName');
    await p.click('#nkNew'); const n2=await p.textContent('#nkName'); console.log('nick',n1,'->',n2);
    await p.screenshot({path:'/tmp/app-nick.png'});
    await p.click('#modalCard [data-act=resume]');
    await p.evaluate(()=>{ best=500; saveLocal(); syncMyScore(); }); await p.waitForTimeout(300);
    console.log('saved doc',JSON.stringify(await p.evaluate(()=>window.__docs.me1&&{e:window.__docs.me1.endless,nk:window.__docs.me1.nk})));
    await p.click('[data-go=rank]'); await p.waitForTimeout(300);
    console.log('rank',(await p.textContent('#rankList')).replace(/\s+/g,' '));
    await p.screenshot({path:'/tmp/app-rank.png'});
    await p.click('#rank [data-go=home]'); await p.click('#acct'); await p.click('#nkHide'); await p.waitForTimeout(200);
    console.log('after hide',Object.keys(await p.evaluate(()=>window.__docs)));
  } else {
    await p.click('[data-go=rank]'); await p.waitForTimeout(200); console.log('rank',await p.textContent('#rankList'));
    await p.click('#rank [data-go=home]'); await p.click('#btnEndless'); await p.waitForTimeout(300); console.log('endless on',await p.$eval('#game',e=>e.classList.contains('on')));
  }
  console.log('errors',errs); await b.close(); srv.close();
})();
