export function evaluateScenario(input: string): string { const[server,client]=input.split("|");return server===client?"hydrate":"rerender" }
