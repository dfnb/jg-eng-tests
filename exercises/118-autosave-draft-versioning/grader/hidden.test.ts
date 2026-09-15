import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","3|3|ok","apply")
check("C02","3|2|ok","ignore")
check("C03","3|4|ok","ignore")
check("C04","3|3|conflict","resolve")
check("C05","3|3|network","retry")
