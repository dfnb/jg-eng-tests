import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "0|1|1", "2");
check("C02", "5|1|1", "7");
check("C03", "5|-2", "3");
check("C04", "4", "4");
check("C05", "0|1|1|1|1", "4");
