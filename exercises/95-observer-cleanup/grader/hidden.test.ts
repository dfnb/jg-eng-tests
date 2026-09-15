import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "observer,cleanup:observer", "clean");
check("C02", "timer,cleanup:timer", "clean");
check("C03", "observer,timer,cleanup:timer", "observer");
check("C04", "observer,timer,cleanup:observer,cleanup:timer", "clean");
check("C05", "", "clean");
