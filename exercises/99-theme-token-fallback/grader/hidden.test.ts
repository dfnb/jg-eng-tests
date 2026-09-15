import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "light|bg", "white");
check("C02", "dark|bg", "black");
check("C03", "dark|accent", "blue");
check("C04", "dark|shadow", "unset");
check("C05", "dark|text", "white");
