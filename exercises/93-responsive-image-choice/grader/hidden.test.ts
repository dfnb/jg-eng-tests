import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "400|1|320,640,1280", "640");
check("C02", "400|2|320,640,1280", "1280");
check("C03", "300|1|320,640", "320");
check("C04", "1000|2|320,640,1280", "1280");
check("C05", "500|1|1280,320,640", "640");
