import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "50|100|sending", "50");
check("C02", "100|100|sending", "100");
check("C03", "120|100|sending", "100");
check("C04", "10|0|sending", "indeterminate");
check("C05", "50|100|cancelled", "cancelled");
