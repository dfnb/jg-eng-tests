import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "q=red&page=2", "q=red&page=2");
check("C02", "q=x&page=0", "q=x&page=1");
check("C03", "q=%20a%20", "q=a&page=1");
check("C04", "q=ação&page=3", "q=a%C3%A7%C3%A3o&page=3");
check("C05", "", "q=&page=1");
