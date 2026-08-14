import fs from 'node:fs/promises';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const OUT = 'C:/Users/ayanb/.codex/visualizations/2026/08/13/019ff91d-15d2-7243-a124-1b56e45eee18/udyaan-output';
const TMP = 'C:/Users/ayanb/.codex/visualizations/2026/08/13/019ff91d-15d2-7243-a124-1b56e45eee18/udyaan-output';
const W = 1280, H = 720;
const C = {
  navy: '#283241', ink: '#1F2933', cream: '#F6F2E9', white: '#FFFFFF',
  muted: '#65707B', line: '#C7C9C8', sage: '#5B806D', blue: '#9FC1CF',
  lavender: '#8E84A6', orange: '#C77B52', pink: '#B97D93', yellow: '#E5D36E',
  paleBlue: '#E6F0F3', paleLav: '#EAE7F0', paleOrange: '#F4E5DB', palePink: '#F2E6EB'
};

function addText(slide, text, x, y, w, h, size=18, color=C.ink, opts={}) {
  const s = slide.shapes.add({ geometry: 'textbox', name: opts.name, position: { left:x, top:y, width:w, height:h }, fill:'none', line:{style:'solid', fill:'none', width:0} });
  s.text = text;
  s.text.style = { fontSize:size, color, bold:!!opts.bold, alignment:opts.align || 'left', verticalAlignment:opts.valign || 'top', italic:!!opts.italic };
  return s;
}
function rect(slide, x,y,w,h, fill, radius='rounded-xl', lineFill='none', lineWidth=0) {
  const cfg = { geometry: radius === 'circle' ? 'ellipse' : 'roundRect', position:{left:x,top:y,width:w,height:h}, fill, line:{style:'solid', fill:lineFill, width:lineWidth} };
  if (radius !== 'circle') cfg.borderRadius = radius;
  return slide.shapes.add(cfg);
}
function line(slide,x1,y1,x2,y2,color=C.line,width=2) {
  return slide.shapes.add({ geometry:'line', position:{left:Math.min(x1,x2),top:Math.min(y1,y2),width:Math.abs(x2-x1),height:Math.abs(y2-y1)}, line:{style:'solid', fill:color, width} });
}
function dot(slide,x,y,r,fill) { return rect(slide,x-r,y-r,2*r,2*r,fill,'circle'); }
function footer(slide, n, dark=false) {
  const col = dark ? '#BCC3CB' : C.muted;
  line(slide,72,666,1208,666,dark?'#5D6673':C.line,1);
  addText(slide,'UDYAAN / FROM IDEA TO BUSINESS',72,678,300,18,11,col,{bold:true});
  addText(slide,String(n).padStart(2,'0'),1168,678,40,18,11,col,{align:'right',bold:true});
}
function header(slide, kicker, title, sub, dark=false) {
  const col = dark ? C.white : C.ink, subcol = dark ? '#D7DCE0' : C.muted;
  addText(slide,kicker.toUpperCase(),72,52,360,20,12,dark?C.yellow:C.sage,{bold:true});
  addText(slide,title,72,86,820,76,36,col,{bold:true});
  if (sub) addText(slide,sub,72,168,870,50,18,subcol,{});
}
function pill(slide,text,x,y,w,fill,color=C.ink) { rect(slide,x,y,w,26,fill,'rounded-lg'); addText(slide,text,x+10,y+5,w-20,16,11,color,{bold:true,align:'center'}); }

function slide1(p) {
  const s=p.slides.add(); s.background.fill=C.navy;
  addText(s,'PROJECT PROPOSAL / COURSE COMPONENT',72,54,360,20,12,C.yellow,{bold:true});
  addText(s,'A course with a map',72,150,560,110,58,C.white,{bold:true});
  addText(s,'A playable navigation layer for Udyaan’s From Idea to Business course.',76,296,470,64,22,'#D7DCE0',{});
  addText(s,'The student still does the real work. The map makes the journey visible, gives each next action a place, and turns evidence into progress.',76,494,520,64,18,'#D7DCE0',{});
  const centers=[[820,250,C.sage,'01','FOGLANDS'],[1000,385,C.lavender,'02','WORKSHOP'],[1142,520,C.orange,'03','ARENA']];
  line(s,820,250,1000,385,'#D7D36E',3); line(s,1000,385,1142,520,'#D7D36E',3);
  for (const [x,y,c,num,label] of centers) { dot(s,x,y,76,c); dot(s,x,y,18,C.navy); addText(s,num,x-16,y-26,32,26,22,C.white,{bold:true,align:'center'}); addText(s,label,x-70,y+88,140,22,13,C.white,{bold:true,align:'center'}); }
  addText(s,'SERIOUS COURSE WORK / PLAYABLE WORLD',816,626,360,18,11,'#BFC6CF',{bold:true,align:'center'});
  footer(s,1,true);
}

function slide2(p) {
  const s=p.slides.add(); s.background.fill=C.cream;
  header(s,'The purpose of the game layer','Every game node must map to a real course action.','This proposal extends the Udyaan course plan with a visual system for orientation, action, evidence, and feedback.');
  const items=[['ORIENTATION','The map shows the current phase, the next action, and the evidence required.',C.sage],['ACTION','Missions convert difficult work into a concrete attempt: talk, test, sell, deliver.',C.orange],['EVIDENCE','Submissions make progress visible and unlock the next business decision.',C.lavender],['PERSISTENCE','Rejection and feedback become information to interpret, not a reason to stop.',C.pink]];
  items.forEach((it,i)=>{ const y=258+i*75; dot(s,92,y+14,10,it[2]); addText(s,it[0],122,y,170,24,15,it[2],{bold:true}); addText(s,it[1],292,y-2,700,44,18,C.ink,{}); line(s,122,y+52,1100,y+52,C.line,1); });
  rect(s,870,108,310,66,C.navy,'rounded-xl'); addText(s,'COURSE LOGIC',892,124,120,16,11,C.yellow,{bold:true}); addText(s,'Lesson → mission → evidence → feedback → next decision',892,146,260,28,15,C.white,{bold:true});
  addText(s,'The map can be strange. The learning must stay specific.',72,596,720,28,22,C.navy,{bold:true});
  footer(s,2);
}

function slide3(p) {
  const s=p.slides.add(); s.background.fill=C.navy;
  header(s,'The course journey','Three regions turn uncertainty into a repeatable business loop.','Each region answers a different question and produces the evidence needed to move forward.',true);
  const xs=[230,640,1050], cs=[C.sage,C.lavender,C.orange], nums=['01','02','03'], titles=['THE FOGLANDS','MAD SCIENTIST WORKSHOP','THE CHAOS ARENA'];
  line(s,xs[0],392,xs[1],392,'#D7D36E',3); line(s,xs[1],392,xs[2],392,'#D7D36E',3);
  xs.forEach((x,i)=>{dot(s,x,392,88,cs[i]); dot(s,x,392,22,C.navy); addText(s,nums[i],x-18,363,36,30,23,C.white,{bold:true,align:'center'}); addText(s,titles[i],x-150,498,300,24,16,C.white,{bold:true,align:'center'});});
  addText(s,'What is the real problem?',88,565,290,26,20,C.blue,{bold:true,align:'center'}); addText(s,'What specific offer could solve it?',490,565,300,26,20,'#D7D36E',{bold:true,align:'center'}); addText(s,'What happens when real people respond?',900,565,300,26,20,'#F1B48A',{bold:true,align:'center'});
  footer(s,3,true);
}

function slide4(p) {
  const s=p.slides.add(); s.background.fill=C.cream;
  header(s,'Region 01 / The Foglands','Find a valuable problem in a real market.','Students narrow a broad interest into a reachable customer group, investigate reality, and state the problem with evidence.');
  rect(s,72,270,380,270,C.paleBlue,'rounded-2xl',C.blue,2); addText(s,'FIELD EVIDENCE',100,294,140,20,12,C.sage,{bold:true});
  const steps=['Choose a specific customer group','Run conversations and collect notes','Measure urgency, cost, and alternatives','Write an evidence-backed problem statement'];
  steps.forEach((t,i)=>{dot(s,112,350+i*46,12,[C.sage,C.blue,C.lavender,C.orange][i]); addText(s,t,140,337+i*46,260,36,17,C.ink,{bold:i===3});});
  addText(s,'MISSION EXAMPLE',530,274,180,20,12,C.orange,{bold:true}); addText(s,'Survive five customer conversations.',530,312,520,42,28,C.ink,{bold:true}); addText(s,'Success is not five yeses. Success is five attempts, useful notes, and a sharper problem hypothesis.',530,370,490,72,19,C.muted,{});
  rect(s,530,484,480,58,C.navy,'rounded-xl'); addText(s,'CHECKPOINT  /  PROBLEM EVIDENCE',550,502,440,22,15,C.white,{bold:true,align:'center'});
  footer(s,4);
}

function slide5(p) {
  const s=p.slides.add(); s.background.fill=C.cream;
  header(s,'Region 02 / Mad Scientist Workshop','Turn evidence into an offer someone could buy.','The “superweapon” is the complete offer: a specific customer, promised result, delivery method, scope, and price logic.');
  const cx=630, cy=410; const nodes=[['CUSTOMER',300,285,C.blue],['PROBLEM\nEVIDENCE',300,500,C.sage],['RESULT',960,285,C.orange],['PRICE +\nDELIVERY',960,500,C.pink]];
  for (const [t,x,y,c] of nodes) { line(s,x+100,y+42,cx,cy,C.line,2); rect(s,x,y,200,84,c,'rounded-2xl'); addText(s,t,x+18,y+26,164,36,18,C.navy,{bold:true,align:'center'}); }
  dot(s,cx,cy,105,C.lavender); addText(s,'OFFER',cx-70,cy-28,140,30,28,C.white,{bold:true,align:'center'}); addText(s,'FIELD-READY',cx-70,cy+10,140,20,13,C.yellow,{bold:true,align:'center'});
  addText(s,'If it tries to solve everything, it explodes.',72,584,620,30,21,C.navy,{bold:true});
  pill(s,'CHECKPOINT  /  CONCRETE OFFER',850,584,300,C.yellow,C.navy);
  footer(s,5);
}

function slide6(p) {
  const s=p.slides.add(); s.background.fill=C.navy;
  header(s,'Region 03 / The Chaos Arena','Test the offer with real people, then adapt.','The superweapon leaves the workshop. Outreach, buying signals, first delivery, and feedback turn every response into market intelligence.',true);
  const xs=[170,445,720,995], labels=[['OUTREACH','Reach a prioritised list'],['BUYING SIGNAL','Ask for payment or commitment'],['FIRST DELIVERY','Deliver the smallest useful version'],['ITERATION','Decide what changes next']];
  line(s,170,386,995,386,'#D7D36E',3);
  xs.forEach((x,i)=>{dot(s,x,386,46,[C.blue,C.yellow,C.orange,C.pink][i]); addText(s,String(i+1).padStart(2,'0'),x-18,372,36,26,18,C.navy,{bold:true,align:'center'}); addText(s,labels[i][0],x-110,470,220,24,15,C.white,{bold:true,align:'center'}); addText(s,labels[i][1],x-120,505,240,40,15,'#D7DCE0',{align:'center'});});
  rect(s,72,578,1136,42,'#364152','rounded-xl'); addText(s,'The arena rewards attempts, interpretation, delivery, and adaptation, not just successful sales.',94,589,1090,20,16,C.white,{bold:true,align:'center'});
  footer(s,6,true);
}

function slide7(p) {
  const s=p.slides.add(); s.background.fill=C.cream;
  header(s,'The learning loop','A map node opens into focused learning and real work.','The interface creates momentum. The lesson page creates concentration. One clear interaction should move the student from the world into the course.');
  const labels=['MAP NODE','LESSON','LOOM / GPT PRACTICE','REAL MISSION','SUBMIT EVIDENCE','FEEDBACK + UNLOCK'];
  labels.forEach((t,i)=>{ const x=100+i*180; if(i<labels.length-1) line(s,x+70,310,x+180,310,C.line,2); dot(s,x+70,310,28,[C.sage,C.blue,C.lavender,C.orange,C.pink,C.yellow][i]); addText(s,String(i+1).padStart(2,'0'),x+58,300,24,20,13,C.navy,{bold:true,align:'center'}); addText(s,t,x,374,140,36,14,C.ink,{bold:true,align:'center'}); });
  rect(s,224,476,832,106,C.white,'rounded-2xl',C.line,2); pill(s,'CALM MODE',250,498,100,C.paleBlue,C.sage); addText(s,'What counts as a real problem?',380,494,470,32,24,C.ink,{bold:true}); addText(s,'Read, practise, then leave the screen to speak to real people.',380,538,500,24,17,C.muted,{}); pill(s,'START MISSION',900,514,120,C.navy,C.white);
  footer(s,7);
}

function slide8(p) {
  const s=p.slides.add(); s.background.fill=C.white;
  header(s,'The visual direction','A formal course interface with a playful, experimental world.','The visual system should make serious work easier to enter, while keeping lessons calm and readable.');
  const cols=[['EDITORIAL','Clear typography, short explanations, structured course information, calm lesson pages.',C.sage],['GAME WORLD','A zoomed-out map, a student avatar, mission nodes, unlocks, status, and visible progress.',C.lavender],['MAD-SCIENTIST DETAIL','Annotated diagrams, field reports, evidence samples, failed prototypes, and strange tools.',C.orange]];
  cols.forEach((it,i)=>{const x=72+i*380; rect(s,x,290,332,192,[C.paleBlue,C.paleLav,C.paleOrange][i],'rounded-2xl'); rect(s,x,290,332,16,it[2],'rounded-xl'); addText(s,it[0],x+22,334,286,26,18,it[2],{bold:true}); addText(s,it[1],x+22,380,286,76,18,C.ink,{});});
  addText(s,'The weirdness belongs around the work. The work itself must remain legible.',72,564,900,30,22,C.navy,{bold:true});
  footer(s,8);
}

function slide9(p) {
  const s=p.slides.add(); s.background.fill=C.navy;
  header(s,'Build plan','Start with one vertical slice before building the whole universe.','The first release should prove the learning loop in one region, then expand only after student behaviour supports it.',true);
  const phases=[['1. DEFINE','Select one Foglands mission, its lesson, artifact, feedback, and unlock.'],['2. PROTOTYPE','Build the map node, calm lesson view, evidence submission, and progress state.'],['3. TEST','Run the slice with a small student group and observe where they stall.'],['4. EXPAND','Add Workshop and Arena routes once the loop is working.']];
  phases.forEach((it,i)=>{const x=72+i*285; rect(s,x,300,250,190,'#354050','rounded-2xl',i===0?C.yellow:'#566273',i===0?2:1); addText(s,it[0],x+20,328,210,24,16,i===0?C.yellow:C.blue,{bold:true}); addText(s,it[1],x+20,374,210,82,17,C.white,{});});
  addText(s,'WHAT WE NEED',72,548,150,22,13,C.yellow,{bold:true}); addText(s,'Curriculum owner  ·  interaction designer  ·  visual designer  ·  prototype builder  ·  student testers',235,545,900,26,18,C.white,{bold:true});
  footer(s,9,true);
}

function slide10(p) {
  const s=p.slides.add(); s.background.fill=C.cream;
  header(s,'Success criteria','The game earns its place through student behaviour.','The test is whether students understand the journey, take more real-world action, and produce stronger evidence for their next decision.');
  const rows=[['ORIENTATION','Can students answer: where am I, what is next, and what must I submit?',C.sage],['ACTION','Do more students complete conversations, outreach, testing, and delivery?',C.orange],['EVIDENCE','Are problem statements, offers, buying signals, and next decisions clearer?',C.lavender],['PERSISTENCE','Do students return after rejection and use feedback to iterate?',C.pink]];
  rect(s,72,270,1136,242,C.white,'rounded-2xl',C.line,2); rows.forEach((r,i)=>{const y=294+i*52; dot(s,100,y+12,9,r[2]); addText(s,r[0],128,y,160,24,14,r[2],{bold:true}); addText(s,r[1],300,y,820,24,17,C.ink,{}); if(i<3) line(s,100,y+40,1178,y+40,C.line,1);});
  addText(s,'PLAYFUL MAP',150,585,130,20,14,C.navy,{bold:true,align:'center'}); addText(s,'→',302,582,40,26,24,C.orange,{bold:true,align:'center'}); addText(s,'MORE ACTION',370,585,130,20,14,C.navy,{bold:true,align:'center'}); addText(s,'→',522,582,40,26,24,C.orange,{bold:true,align:'center'}); addText(s,'BETTER EVIDENCE',590,585,160,20,14,C.navy,{bold:true,align:'center'}); addText(s,'→',772,582,40,26,24,C.orange,{bold:true,align:'center'}); addText(s,'BETTER DECISIONS',840,585,170,20,14,C.navy,{bold:true,align:'center'});
  footer(s,10);
}

async function writeBlob(path, blob) { await fs.writeFile(path, new Uint8Array(await blob.arrayBuffer())); }
async function main() {
  await fs.mkdir(OUT,{recursive:true}); await fs.mkdir(TMP,{recursive:true});
  const p=Presentation.create({slideSize:{width:W,height:H}});
  [slide1,slide2,slide3,slide4,slide5,slide6,slide7,slide8,slide9,slide10].forEach(fn=>fn(p));
  for (const [i,s] of p.slides.items.entries()) { await writeBlob(`${TMP}/slide-${String(i+1).padStart(2,'0')}.png`, await p.export({slide:s,format:'png',scale:1})); await fs.writeFile(`${TMP}/slide-${String(i+1).padStart(2,'0')}.layout.json`, await (await s.export({format:'layout'})).text()); }
  await writeBlob(`${TMP}/montage.webp`, await p.export({format:'webp',montage:true,scale:1}));
  const pptx=await PresentationFile.exportPptx(p); await pptx.save(`${OUT}/Udyaan_Playable_Course_Proposal_Revised.pptx`);
  console.log((await p.inspect({kind:'slide,textbox,shape',maxChars:6000})).ndjson);
}
main().catch(e=>{console.error(e);process.exitCode=1;});
