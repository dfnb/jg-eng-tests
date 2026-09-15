export function evaluateScenario(input: string): string { const[preference,effect]=input.split("|");if(preference==="reduce")return"instant";return effect==="progress"?"animated-progress":"animate" }
