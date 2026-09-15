import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "a|a|b", "remote:b");
check("C02", "a|b|a", "local:b");
check("C03", "a|b|b", "merged:b");
check("C04", "a|b|c", "conflict:b:c");
check("C05", "a|a|a", "remote:a");
