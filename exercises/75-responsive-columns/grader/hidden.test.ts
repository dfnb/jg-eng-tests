import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "320", "name,actions");
check("C02", "479", "name,actions");
check("C03", "600", "name,status,actions");
check("C04", "1200", "name,status,owner,updated,actions");
check("C05", "800", "name,status,owner,updated,actions");
