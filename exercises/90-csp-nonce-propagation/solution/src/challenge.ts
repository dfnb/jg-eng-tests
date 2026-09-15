export function evaluate(input: string): string { const[trusted,nonce]=input.split("|");return trusted==="yes"&&nonce?`nonce=${nonce}`:"blocked" }
