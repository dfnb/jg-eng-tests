import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "dirty|navigate", "confirm");
check("C02", "clean|navigate", "allow");
check("C03", "dirty|save", "allow");
check("C04", "dirty|close", "confirm");
check("C05", "unknown|navigate", "allow");
