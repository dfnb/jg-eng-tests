import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "pt|1", "1 item");
check("C02", "pt|2", "2 itens");
check("C03", "pt|0", "0 itens");
check("C04", "en|1", "1 item");
check("C05", "en|5", "5 items");
