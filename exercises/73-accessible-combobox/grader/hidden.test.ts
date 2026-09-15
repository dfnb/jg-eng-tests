import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "ap|Apple|Apple|Pear", "Apple:Apple");
check("C02", "pe|Apple|Apple|Pear", "Pear:Pear");
check("C03", "zz|Apple|Apple|Pear", "none:");
check("C04", "|Pear|Apple|Pear", "Pear:Apple,Pear");
check("C05", "a|none|Alpha|Beta", "Alpha:Alpha,Beta");
