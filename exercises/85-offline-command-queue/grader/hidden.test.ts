import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "update:a,update:a", "update:a");
check("C02", "update:a,delete:a", "delete:a");
check("C03", "delete:a,update:a", "delete:a");
check("C04", "update:a,update:b", "update:a,update:b");
check("C05", "", "");
