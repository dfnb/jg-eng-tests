export function evaluate(input: string): string { const w=Number(input);return w<480?"name,actions":w<800?"name,status,actions":"name,status,owner,updated,actions" }
