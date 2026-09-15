import test from "node:test";
    import assert from "node:assert/strict";
    import { evaluate } from "../src/challenge.ts";
    test("contrato público", () => assert.equal(typeof evaluate("update:a,update:a"), "string"));
