export function evaluate(input: string): string { const[items,id,value]=input.split("|");return items.split(",").map(x=>{const[k,v]=x.split(":");return k===id?`${k}:${value}`:x}).join(",") }
