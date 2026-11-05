const load = () => { try{ return JSON.parse(localStorage.getItem("mockDb")||"{}"); }catch(e){ return {}; } };
const store = () => window.__db || (window.__db = load());
const persist = () => localStorage.setItem("mockDb", JSON.stringify(store()));
const L = window.__fsl || (window.__fsl = []);
export function getFirestore(){ return {}; }
export function doc(db, ...p){ return {type:"doc", path:p.join("/")}; }
export function collection(db, ...p){ return {type:"coll", path:p.join("/")}; }
const DEL = {__del:true};
export function deleteField(){ return DEL; }
export class FieldPath{ constructor(...s){ this.segs = s; } }
function fire(){ setTimeout(()=>L.forEach(l=>l()), 0); }
const clone = x => JSON.parse(JSON.stringify(x));
function uidOf(){ try{ return JSON.parse(localStorage.getItem("mockUser")||"null"); }catch(e){ return null; } }
function allowed(path, write){ const u = uidOf(); if(!u) return false; if(u.email==="zekacademy@app.zekacademy.com") return true; const [c,id] = path.split("/"); if(c==="settings") return !write; if(c==="students") return id===u.uid; if(c==="notifs") return write; if(c==="sorular"||c==="soruFoto") return true; if(c==="koc") return !write; return false; }
function deny(){ const e = new Error("denied"); e.code="permission-denied"; return e; }
export async function setDoc(ref, data){ if(!allowed(ref.path,true)) throw deny(); store()[ref.path] = clone(data); persist(); fire(); }
export async function updateDoc(ref, ...args){ if(!allowed(ref.path,true)) throw deny(); const d = store()[ref.path]; if(!d) throw new Error("no doc");
  for(let i=0;i<args.length;i+=2){ const segs = args[i].segs, v = args[i+1]; let o = d; for(let j=0;j<segs.length-1;j++){ if(!o[segs[j]] || typeof o[segs[j]]!=="object") o[segs[j]] = {}; o = o[segs[j]]; } if(v===DEL) delete o[segs[segs.length-1]]; else o[segs[segs.length-1]] = clone(v); }
  window.__updates = (window.__updates||0)+1; persist(); fire(); }
export async function deleteDoc(ref){ delete store()[ref.path]; persist(); fire(); }
export function query(ref, ...w){ return {...ref, where:w}; }
export function where(f, op, v){ return {f, op, v}; }
export async function getDoc(ref){ const d = store()[ref.path]; return {exists:()=>!!d, data:()=>clone(d)}; }
export function onSnapshot(ref, next, err){
  const run = () => {
    if(ref.type==="doc"){ if(!allowed(ref.path,false)){ err && err(deny()); return; } const d = store()[ref.path]; next({exists:()=>!!d, data:()=>clone(d)}); }
    else { const pre = ref.path+"/"; if(ref.path==="students" && !(uidOf()?.email==="zekacademy@app.zekacademy.com")){ err && err(deny()); return; } const docs = Object.keys(store()).filter(k=>k.startsWith(pre) && k.split("/").length===2).filter(k=>!(ref.where||[]).some(w=>store()[k][w.f]!==w.v)).map(k=>({id:k.slice(pre.length), data:()=>clone(store()[k])})); next({docs}); }
  };
  L.push(run); setTimeout(run, 0); return ()=>{ const i = L.indexOf(run); if(i>=0) L.splice(i,1); };
}
