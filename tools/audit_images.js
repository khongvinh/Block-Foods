// Quét mọi hình .ic: báo hình nào vượt khỏi khung chứa trực tiếp
const {chromium}=require('playwright');
const D=__dirname+'/';  // chạy: node tools/audit_images.js (cần Playwright)
async function audit(p,label){
  return await p.evaluate(label=>{
    const out=[];
    document.querySelectorAll('.screen.on img.ic, #modal.on img.ic, #drag img.ic').forEach(img=>{
      const r=img.getBoundingClientRect(); if(!r.width) return;
      // khung chứa: ô thớt/ô khay/nút/chip gần nhất
      const box=img.closest('.tile,.pc,.slot2,.ingbtn,.chip,.plate,.bill,.kpan,.big,.who,.face,.order-dish,.bigE,.btn,.tab,.rate,.qbadge,.moves,.lb-row,.ings span,.order-ings span,.e,.pill')||img.parentElement;
      const b=box.getBoundingClientRect(); const tol=2;
      if(r.left<b.left-tol||r.right>b.right+tol||r.top<b.top-tol||r.bottom>b.bottom+tol)
        out.push(`${label}: ${img.src.split('/').pop()} img ${Math.round(r.width)}x${Math.round(r.height)} vượt khung .${box.className.split(' ')[0]} ${Math.round(b.width)}x${Math.round(b.height)}`);
    });
    return out;
  },label);
}
(async()=>{
const b=await chromium.launch(); const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[]; p.on('pageerror',e=>errs.push(e.stack.split('\n').slice(0,3).join(' / ')));
await p.addInitScript(()=>localStorage.setItem('bf_progress',JSON.stringify({stars:Object.fromEntries(["trungChien","comTam","banhMi","pho","bunCha","goiCuon","canhChua","banhXeo","caKho","bunBo","canhNam","comChien"].map(k=>[k,3])),reviews:{pho:{n:1,sum:4,log:[{c:"tay",r:4,n:["Món ngon"],t:Date.now()}]}}})));
await p.goto('file:///home/user/Block-Foods/index.html');
let issues=[];
const ALL=Object.keys(await p.evaluate(()=>({trung:1,hanh:1,com:1,suon:1,duaLeo:1,banhMi:1,thit:1,ot:1,pho:1,rauThom:1,bun:1,rauSong:1,banhTrang:1,tom:1,ca:1,caChua:1,thom:1,botGao:1,gia:1,toi:1,nuocMau:1,chanh:1,nam:1,dauHu:1})));
for(let lv=0;lv<12;lv++){
  await p.evaluate(({lv,ALL})=>{ document.querySelector('#modal').classList.remove('on'); __BF.startLevel(lv); const G=__BF.G;
    let i=0; for(let r=0;r<8;r++)for(let c=0;c<8;c++) if((r+c)%2) G.grid[r][c]=ALL[(i++)%ALL.length];
    G.tray=[{shape:{cells:[[0,0],[0,1],[1,0]],h:2,w:2},ing:ALL[lv*2%24]},{shape:{cells:[[0,0],[1,0],[2,0]],h:3,w:1},ing:ALL[(lv*2+1)%24]},{shape:{cells:[[0,0]],h:1,w:1},ing:"thom"}];
    G.grid[0][0]=null; __BF.place(2,0,0); },{lv,ALL});
  await p.waitForTimeout(150);
  issues.push(...await audit(p,'game'+lv));
}
await p.screenshot({path:D+'aud-game.png'});
// cook order screens (xếp nhân) & customer card, menu, rank, review popup, checkout
for(const id of ["comTam","banhMi","bunCha","goiCuon"]){
  await p.evaluate(id=>{ const D=__BF.G && 0; },id);
  await p.evaluate(id=>{ startCooking(DISHES.find(d=>d.id===id),()=>{}); },id); await p.waitForTimeout(200);
  issues.push(...await audit(p,'cook-'+id));
}
await p.evaluate(()=>startCooking(DISHES[0],()=>{})); await p.waitForTimeout(200); issues.push(...await audit(p,'cook-hold'));
await p.evaluate(()=>startCooking(DISHES[3],()=>{})); await p.waitForTimeout(200); issues.push(...await audit(p,'cook-timing'));
await p.evaluate(()=>{ G.customer=null; }).catch(()=>{});
await p.evaluate(()=>{ document.querySelector('#modal').classList.remove('on'); newOrder(); }); await p.waitForTimeout(300); issues.push(...await audit(p,'order'));
await p.evaluate(()=>startCheckout(DISHES[9],{k:"good",label:IMG("ui-smile")+" Ngon",tip:.1},()=>{})); await p.waitForTimeout(200);
for(const v of [50000,20000,10000,5000]) { const bt=await p.$(`.bills .bill[data-v="${v}"]`); if(bt) await bt.click(); }
issues.push(...await audit(p,'checkout'));
await p.evaluate(()=>show('book')); await p.waitForTimeout(200); issues.push(...await audit(p,'menu'));
await p.evaluate(()=>showReviews('pho')); await p.waitForTimeout(200); issues.push(...await audit(p,'reviews'));
await p.evaluate(()=>{document.querySelector('#modal').classList.remove('on'); show('rank');}); issues.push(...await audit(p,'rank'));
await p.evaluate(()=>__BF.startEndless()); await p.waitForTimeout(200); issues.push(...await audit(p,'endless'));
console.log(issues.length? [...new Set(issues)].join('\n') : 'Không có hình nào tràn khung'); console.log(errs);
await b.close();})();
