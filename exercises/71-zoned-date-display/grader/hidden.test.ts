import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "2025-01-02T02:00:00Z|-180", "2025-01-01");
check("C02", "2025-01-02T02:00:00Z|0", "2025-01-02");
check("C03", "2025-01-01T23:00:00Z|120", "2025-01-02");
check("C04", "2025-05-01T03:00:00Z|-180", "2025-05-01");
check("C05", "2025-01-01T01:00:00Z|-120", "2024-12-31");
