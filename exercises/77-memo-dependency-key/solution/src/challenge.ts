export function evaluate(input: string): string { const[user,locale,items]=input.split("|");return`${user}:${locale}:${items.split(",").sort().join(",")}` }
