export function evaluate(input: string): string { const[current,result]=input.split("|").map(Number);return result===current?"apply":"ignore" }
