import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","commerce.order|v2|id,timestamp,total","accept")
check("C02","profile.user|v2|id,timestamp","foreign")
check("C03","commerce.order|v1|id,timestamp","unsupported")
check("C04","commerce.order|v2|timestamp","invalid")
check("C05","commerce.order|v2|id","invalid")
