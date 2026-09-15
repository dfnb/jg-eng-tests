export function evaluate(input: string): string { const[lang,n0]=input.split("|");const n=Number(n0);if(lang==="pt")return`${n} ${n===1?"item":"itens"}`;return`${n} ${n===1?"item":"items"}` }
