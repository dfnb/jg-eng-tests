import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "mount,unmount", "clean");
check("C02", "mount", "leak:1");
check("C03", "mount,mount,unmount,unmount", "clean");
check("C04", "unmount", "invalid");
check("C05", "mount,mount,unmount", "leak:1");
