import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "a:1,b:1|c:1", "a:1,b:1,c:1");
check("C02", "a:1,b:1|b:2,c:1", "a:1,b:2,c:1");
check("C03", "a:1|", "a:1");
check("C04", "|a:1", "a:1");
check("C05", "a:1|a:2,a:3", "a:3");
