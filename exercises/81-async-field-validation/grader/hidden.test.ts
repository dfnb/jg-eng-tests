import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "3|3", "apply");
check("C02", "3|2", "ignore");
check("C03", "3|4", "ignore");
check("C04", "1|1", "apply");
check("C05", "0|0", "apply");
