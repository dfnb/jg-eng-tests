import { readdirSync, statSync } from "node:fs"
    import { join } from "node:path"
    import { spawnSync } from "node:child_process"
    import { fileURLToPath } from "node:url"
    const walk = directory => readdirSync(directory).flatMap(name => { const path=join(directory,name); return statSync(path).isDirectory()?walk(path):[path] })
    const files=walk(fileURLToPath(new URL("../src",import.meta.url))).filter(path=>path.endsWith(".ts")&&!path.endsWith(".component.ts"))
    const failures=files.filter(path=>spawnSync(process.execPath,["--check",path],{stdio:"ignore"}).status!==0)
    if(failures.length){console.error(failures.join("\n"));process.exit(1)}
    console.log(`syntax OK: ${files.length} TypeScript modules`)
