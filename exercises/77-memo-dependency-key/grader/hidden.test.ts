import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "u1|pt|b,a", "u1:pt:a,b");
check("C02", "u1|en|a", "u1:en:a");
check("C03", "u|pt|c,a,b", "u:pt:a,b,c");
check("C04", "u|pt|", "u:pt:");
check("C05", "u2|pt|a", "u2:pt:a");
