import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "POST|app.test|app.test|abc", "token:abc");
check("C02", "GET|app.test|app.test|abc", "none");
check("C03", "POST|app.test|api.other|abc", "none");
check("C04", "POST|app.test|app.test|", "none");
check("C05", "DELETE|app.test|app.test|x", "token:x");
