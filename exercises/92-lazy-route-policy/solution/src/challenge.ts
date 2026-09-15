export function evaluate(input: string): string { const[route,mode]=input.split("|");return route.startsWith("/admin")&&mode!=="lazy"?"violation":"ok" }
