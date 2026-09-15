import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","set:a,set:b,undo","a")
check("C02","set:a,set:b,undo,redo","b")
check("C03","set:a,set:b,undo,set:c,redo","c")
check("C04","undo","empty")
check("C05","set:a,set:b,set:c,undo,undo","a")
