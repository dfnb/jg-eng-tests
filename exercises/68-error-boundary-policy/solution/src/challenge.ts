export function evaluate(input: string): string { const[k,retries]=input.split("|");return k==="auth"?"login":k==="network"&&Number(retries)<2?"retry":"fallback" }
