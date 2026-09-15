import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","a,b,c|remove:b","a,c")
check("C02","a,b|add:c","a,b,c")
check("C03","a,c|add:b:1","a,b,c")
check("C04","a,b|add:b","a,b")
check("C05","a,b|remove:x","a,b")
