import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","a:old,b:same|a:new","a:new,b:same")
check("C02","a:one|b:two","a:one,b:two")
check("C03","b:two|a:one","a:one,b:two")
check("C04","|a:one","a:one")
check("C05","a:one|a:","a:")
