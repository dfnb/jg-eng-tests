import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "/admin|lazy", "ok");
check("C02", "/admin|eager", "violation");
check("C03", "/admin/users|eager", "violation");
check("C04", "/|eager", "ok");
check("C05", "/login|eager", "ok");
