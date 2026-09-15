import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "editing|submit", "submitting");
check("C02", "submitting|success", "done");
check("C03", "submitting|failure", "editing");
check("C04", "done|reset", "editing");
check("C05", "done|submit", "done");
