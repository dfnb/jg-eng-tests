import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "yes|250|0|no", "loading");
check("C02", "yes|50|0|no", "idle");
check("C03", "no|0|0|no", "empty");
check("C04", "no|0|3|no", "success");
check("C05", "yes|500|0|yes", "error");
