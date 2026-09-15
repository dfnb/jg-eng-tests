import test from "node:test"
    import assert from "node:assert/strict"
    import { executeScenario } from "../src/app/public-api.ts"
    test("public facade", () => assert.equal(executeScenario("0|0:A"), "1|A"))
