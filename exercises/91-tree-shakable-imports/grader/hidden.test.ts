import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "lodash/debounce", "granular");
check("C02", "lodash", "heavy");
check("C03", "icons/all", "heavy");
check("C04", "lib/index", "heavy");
check("C05", "date-fns/format", "granular");
