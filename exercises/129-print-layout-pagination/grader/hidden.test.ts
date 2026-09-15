import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","100|20,30,40","1")
check("C02","100|60,50","2")
check("C03","50|30,30,30","3")
check("C04","50|50,1","2")
check("C05","50|51","oversize")
