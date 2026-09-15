import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "0|no", "1000");
check("C02", "1|no", "2000");
check("C03", "5|no", "30000");
check("C04", "10|no", "30000");
check("C05", "8|yes", "1000");
