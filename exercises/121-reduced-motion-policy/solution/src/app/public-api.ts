import { evaluateScenario } from "../features/scenario/scenario-policy.ts"
    export function executeScenario(input: string): string {
      if (typeof input !== "string") throw new TypeError("input must be a string")
      return evaluateScenario(input)
    }
