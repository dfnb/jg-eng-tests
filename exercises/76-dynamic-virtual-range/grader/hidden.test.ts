import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "0|30|1|10,20,30,40", "0-3");
check("C02", "30|30|0|10,20,30,40", "2-3");
check("C03", "30|30|1|10,20,30,40", "1-4");
check("C04", "5|5|0|10,10", "0-1");
check("C05", "50|100|2|10,20,30", "0-3");
