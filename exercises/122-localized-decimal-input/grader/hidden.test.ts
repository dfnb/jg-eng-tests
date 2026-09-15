import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","pt-BR|1.234,56","1234.56")
check("C02","en-US|1,234.56","1234.56")
check("C03","pt-BR|10","10.00")
check("C04","en-US|abc","invalid")
check("C05","pt-BR| 2,5 ","2.50")
