import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "event|ready", "pass");
check("C02", "poll|ready", "pass");
check("C03", "sleep|ready", "flaky");
check("C04", "event|loading", "flaky");
check("C05", "timeout|ready", "flaky");
