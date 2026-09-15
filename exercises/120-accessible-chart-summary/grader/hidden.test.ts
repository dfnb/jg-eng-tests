import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","1,3,5","up|min=1|max=5")
check("C02","5,3,1","down|min=1|max=5")
check("C03","2,5,2","flat|min=2|max=5")
check("C04","7","flat|min=7|max=7")
check("C05","","empty")
