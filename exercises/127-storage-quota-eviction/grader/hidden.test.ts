import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","100|10|a:20:5:no","none")
check("C02","50|20|a:20:9:no,b:20:1:no","a")
check("C03","50|30|a:20:9:no,b:20:8:no,c:20:1:no","a,b")
check("C04","30|20|a:20:9:yes","quota-error")
check("C05","20|20|","none")
