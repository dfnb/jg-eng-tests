import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","a,b|a,b","hydrate")
check("C02","a,b|b,a","hydrate")
check("C03","a|a,b","rerender")
check("C04","a,b|a","rerender")
check("C05","|","hydrate")
