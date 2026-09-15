import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "network|0", "retry");
check("C02", "network|2", "fallback");
check("C03", "auth|0", "login");
check("C04", "render|0", "fallback");
check("C05", "fatal|5", "fallback");
