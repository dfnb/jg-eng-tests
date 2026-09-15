import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "https://example.com", "https://example.com");
check("C02", "mailto:a@example.com", "mailto:a@example.com");
check("C03", "javascript:alert(1)", "#");
check("C04", "/orders", "/orders");
check("C05", "//evil.test", "#");
