import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","0|0:A","1|A")
check("C02","0|1:B","0|wait")
check("C03","0|1:B,0:A,2:C","3|ABC")
check("C04","2|2:C,3:D","4|CD")
check("C05","4|","4|wait")
