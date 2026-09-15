import test from "node:test";
import assert from "node:assert/strict";
const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");
function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }
check("C01", "<script>x</script>", "&lt;script&gt;x&lt;/script&gt;");
check("C02", "A&B", "A&amp;B");
check("C03", "\"x\"", "&quot;x&quot;");
check("C04", "'x'", "&#39;x&#39;");
check("C05", "ação", "ação");
