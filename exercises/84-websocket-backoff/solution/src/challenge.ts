export function evaluate(input: string): string { const[attempt,stable]=input.split("|");return stable==="yes"?"1000":String(Math.min(30000,1000*2**Number(attempt))) }
