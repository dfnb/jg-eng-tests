export function evaluate(input: string): string { const[strategy,state]=input.split("|");return strategy==="poll"&&state==="ready"?"pass":strategy==="event"&&state==="ready"?"pass":"flaky" }
