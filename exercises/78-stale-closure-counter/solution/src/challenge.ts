export function evaluate(input: string): string { const[start,...deltas]=input.split("|").map(Number);return String(deltas.reduce((n,d)=>n+d,start)) }
