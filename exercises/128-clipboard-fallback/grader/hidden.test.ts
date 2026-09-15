import test from "node:test"
import assert from "node:assert/strict"
const { executeScenario } = await import(process.env.CHALLENGE_TARGET + "/src/app/public-api.ts")
function check(id,input,expected){test(id,()=>{try{assert.equal(executeScenario(input),expected);console.log(id+"|pass")}catch(error){console.log(id+"|fail|"+error.message);throw error}})}
check("C01","yes|yes|granted","clipboard-api")
check("C02","no|yes|granted","selection-fallback")
check("C03","yes|no|prompt","selection-fallback")
check("C04","yes|yes|denied","manual")
check("C05","yes|yes|prompt","clipboard-api")
