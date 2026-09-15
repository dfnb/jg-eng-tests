import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "yes|abc", "nonce=abc");
check("C02", "no|abc", "blocked");
check("C03", "yes|", "blocked");
check("C04", "yes|A-B_1", "nonce=A-B_1");
check("C05", "no|", "blocked");
