export function evaluate(input: string): string { const[pending,action]=input.split("|");return pending==="dirty"&&action!=="save"?"confirm":"allow" }
