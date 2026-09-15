import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "a,b,c|c|a", "c,a,b");
check("C02", "a,b,c|a|end", "b,c,a");
check("C03", "x,a,b,c|c|b", "x,a,c,b");
check("C04", "a,b|c|b", "a,c,b");
check("C05", "a,b|b|x", "b,a");
