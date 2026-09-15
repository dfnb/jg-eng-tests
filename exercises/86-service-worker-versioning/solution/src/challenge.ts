export function evaluate(input: string): string { const[current,keys]=input.split("|");return keys.split(",").filter(k=>k.startsWith("app-")&&k!==`app-${current}`).sort().join(",") }
