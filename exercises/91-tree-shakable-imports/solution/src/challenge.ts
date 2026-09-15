export function evaluate(input: string): string { return input.includes("/all")||input.endsWith("/index")||input==="lodash"?"heavy":"granular" }
