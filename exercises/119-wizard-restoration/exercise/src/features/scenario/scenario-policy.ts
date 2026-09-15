export function evaluateScenario(input: string): string { const[saved]=input.split("|");return String(Math.max(0,Number(saved))) }
