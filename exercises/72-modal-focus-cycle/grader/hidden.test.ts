import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "0|3|Tab", "1");
check("C02", "2|3|Tab", "0");
check("C03", "0|3|ShiftTab", "2");
check("C04", "1|3|Escape", "restore");
check("C05", "0|0|Tab", "container");
