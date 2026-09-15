import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","reduce|modal","instant")
check("C02","reduce|progress","static-progress")
check("C03","normal|modal","animate")
check("C04","normal|progress","animated-progress")
check("C05","reduce|sparkle","instant")
