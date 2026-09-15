import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","1|yes,no,no","1")
check("C02","2|no,no,no","0")
check("C03","3|yes,yes,no,yes","2")
check("C04","3|yes,yes,yes","3")
check("C05","-1|yes","0")
