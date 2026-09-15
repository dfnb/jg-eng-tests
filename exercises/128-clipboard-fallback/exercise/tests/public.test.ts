import test from "node:test"
    import assert from "node:assert/strict"
    import { executeScenario } from "../src/app/public-api.ts"
    test("public facade", () => assert.equal(executeScenario("yes|yes|granted"), "clipboard-api"))
