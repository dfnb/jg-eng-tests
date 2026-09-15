export function evaluate(input: string): string { const[iso,offset]=input.split("|");const d=new Date(Date.parse(iso)+Number(offset)*60000);return d.toISOString().slice(0,10) }
