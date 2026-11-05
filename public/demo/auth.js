const M = window.__mock || (window.__mock = { users:{}, db:{}, listeners:[] });
const auths = {};
function mk(app){ return auths[app.name] || (auths[app.name] = { app, currentUser:null, cbs:[] }); }
export function getAuth(app){ const a = mk(app); if(app.name==="[DEFAULT]" && !a.restored){ a.restored = true; try{ const u = JSON.parse(localStorage.getItem("mockUser")||"null"); if(u) a.currentUser = {...u}; }catch(e){} } return a; }
export function initializeAuth(app){ return mk(app); }
export const inMemoryPersistence = "mem", browserLocalPersistence = "local", browserSessionPersistence = "session";
export async function setPersistence(){ }
const users = () => { try{ return JSON.parse(localStorage.getItem("mockUsers")||"{}"); }catch(e){ return {}; } };
const saveUsers = u => localStorage.setItem("mockUsers", JSON.stringify(u));
function setUser(a, u){ a.currentUser = u; if(a.app.name==="[DEFAULT]") localStorage.setItem("mockUser", JSON.stringify(u)); setTimeout(()=>a.cbs.forEach(cb=>cb(u)), 0); }
export function onAuthStateChanged(a, cb){ a.cbs.push(cb); setTimeout(()=>cb(a.currentUser), 0); return ()=>{}; }
export async function signInWithEmailAndPassword(a, email, p){ const u = users()[email]; if(!u || u.p!==p){ const e = new Error("bad"); e.code="auth/invalid-credential"; throw e; } setUser(a, {uid:u.uid, email}); return {user:a.currentUser}; }
export async function createUserWithEmailAndPassword(a, email, p){ const us = users(); if(us[email]){ const e = new Error("x"); e.code="auth/email-already-in-use"; throw e; } const uid = "u"+Math.random().toString(36).slice(2,10); us[email] = {uid, p}; saveUsers(us); setUser(a, {uid, email}); return {user:a.currentUser}; }
export async function signOut(a){ a.currentUser = null; if(a.app.name==="[DEFAULT]") localStorage.removeItem("mockUser"); setTimeout(()=>a.cbs.forEach(cb=>cb(null)),0); }
export async function updatePassword(user, p){ const us = users(); us[user.email].p = p; saveUsers(us); }
export const EmailAuthProvider = { credential:(email,p)=>({email,p}) };
export async function reauthenticateWithCredential(user, c){ if(users()[c.email]?.p !== c.p){ const e = new Error("x"); e.code="auth/invalid-credential"; throw e; } }
