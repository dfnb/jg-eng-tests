import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "2|app-1,app-2", "app-1");
check("C02", "2|other-1,app-2", "");
check("C03", "3|app-1,app-2,app-3", "app-1,app-2");
check("C04", "1|", "");
check("C05", "x|app-x", "");
