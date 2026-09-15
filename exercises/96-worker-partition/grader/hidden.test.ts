import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "10|2", "5,5");
check("C02", "10|3", "4,3,3");
check("C03", "2|4", "1,1");
check("C04", "0|4", "");
check("C05", "5|0", "5");
