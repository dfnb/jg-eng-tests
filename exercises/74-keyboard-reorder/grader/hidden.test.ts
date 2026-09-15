import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "a,b,c|b|up", "b,a,c");
check("C02", "a,b,c|b|down", "a,c,b");
check("C03", "a,b|a|up", "a,b");
check("C04", "a,b|b|down", "a,b");
check("C05", "a,b|x|up", "a,b");
