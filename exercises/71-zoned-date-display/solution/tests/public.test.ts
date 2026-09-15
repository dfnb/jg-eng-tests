import test from "node:test";
    import assert from "node:assert/strict";
    import { evaluate } from "../src/challenge.ts";
    test("contrato público", () => assert.equal(typeof evaluate("2025-01-02T02:00:00Z|-180"), "string"));
