#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

from extended_definitions import FRONTEND
from generate_frontend_exercises import RUN

ROOT = Path(__file__).resolve().parents[1]


def clean(value: str) -> str:
    return dedent(value).strip() + "\n"


def write(path: Path, value: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(value))
    if executable:
        path.chmod(0o755)


def js(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def lockfile(name: str, framework: str) -> str:
    canonical = "07-accessible-checkout" if framework == "react" else "09-slow-dashboard"
    source = ROOT / "exercises" / canonical / "solution" / "package-lock.json"
    data = json.loads(source.read_text())
    data["name"] = name
    data["packages"][""]["name"] = name
    return json.dumps(data, ensure_ascii=False, indent=2)


def generate(item: dict) -> None:
    name = f"{item['id']}-{item['slug']}"
    root = ROOT / "exercises" / name
    framework = item["framework"]
    dependencies = {"react": "19.3.0", "react-dom": "19.3.0"} if framework == "react" else {
        "@angular/core": "22.1.6", "@angular/forms": "22.1.6", "rxjs": "7.8.2"
    }
    package = {
        "name": name,
        "private": True,
        "version": "1.0.0",
        "type": "module",
        "scripts": {"test": "node tests/public.test.ts", "lint": "node --check src/challenge.ts"},
        "dependencies": dependencies,
        "devDependencies": {"typescript": "7.0.2"},
    }
    broken = 'export function evaluate(input: string): string { return "<unimplemented>" }'
    solution = f"export function evaluate(input: string): string {{ {item['body']} }}"
    if framework == "react":
        component_path = "src/App.tsx"
        component = """import React, { useState } from "react";
        import { evaluate } from "./challenge";

        export function App() {
          const [input, setInput] = useState("");
          return <main><h1>Laboratório</h1><label htmlFor="case">Entrada</label><input id="case" value={input} onChange={e => setInput(e.target.value)} /><output aria-live="polite">{evaluate(input)}</output></main>;
        }
        """
    else:
        component_path = "src/app.component.ts"
        component = """import { Component } from "@angular/core";
        import { evaluate } from "./challenge";

        @Component({selector: "app-root", standalone: true, template: `<main><h1>Laboratório</h1><label for="case">Entrada</label><input id="case" #value (input)="output=evaluate(value.value)"><output aria-live="polite">{{output}}</output></main>`})
        export class AppComponent { output=""; evaluate=evaluate; }
        """
    public_input = js(item["cases"][0][1])
    public = f"""import test from "node:test";
    import assert from "node:assert/strict";
    import {{ evaluate }} from "../src/challenge.ts";
    test("contrato público", () => assert.equal(typeof evaluate({public_input}), "string"));
    """
    hidden = [
        'import test from "node:test";',
        'import assert from "node:assert/strict";',
        'const { evaluate } = await import(process.env.CHALLENGE_TARGET + "/src/challenge.ts");',
        'function check(id, input, expected) { test(id, () => { try { assert.equal(evaluate(input), expected); console.log(id+"|pass") } catch(error) { console.log(id+"|fail|"+error.message); throw error } }) }',
    ]
    checks = []
    for index, (description, input_value, expected) in enumerate(item["cases"], 1):
        criterion = f"C{index:02d}"
        hidden.append(f"check({js(criterion)}, {js(input_value)}, {js(expected)});")
        checks.append({
            "id": criterion,
            "level": "minimum" if index <= 3 else "intermediate" if index == 4 else "desired",
            "weight": 3 if index == 1 else 2 if index <= 4 else 1,
            "description": description,
        })
    setup = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    cd "$root"
    npm ci --ignore-scripts
    """
    test_script = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    cd "$root"
    npm test
    """
    lint = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    cd "$root"
    npm run lint
    """
    readme = f"""# {item['title']}

    Este repositório simula uma parte isolada de uma aplicação {framework.title()}. A interface demonstra o uso da política e a função em `src/challenge.ts` concentra o contrato testável.

    ## Stack

    {framework.title()}, TypeScript e Node.js 24.15.0, fixado em `.node-version`.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    A API e os eventos de navegador são representados por fixtures locais. Nenhuma credencial ou serviço externo é necessário.
    """
    challenge = f"""# Desafio: {item['title']}

    ## Contexto

    {item['summary']}

    ## Pedido

    Complete `evaluate` preservando sua exportação e integre a decisão ao componente quando isso for relevante. Considere os limites naturais de **{item['focus']}**, não somente o caminho mais comum.

    ## Restrições

    Mantenha TypeScript, {framework.title()} e o formato textual do contrato. Não adicione chamadas de rede, dependências ou respostas codificadas para fixtures específicas.

    ## Verificação

    Execute `./scripts/test.sh` e `./scripts/lint.sh`. A avaliação privada contém entradas adicionais, inclusive casos de borda.
    """
    rows = []
    for check in checks:
        level = {"minimum": "mínimo", "intermediate": "intermediário", "desired": "desejado"}[check["level"]]
        rows.append(f"| {check['id']} | {level} | {check['weight']} | {check['description']} | teste privado `{check['id']}` |")
    evaluation = f"""# Avaliação: {item['title']}

    - **ID:** {item['id']}
    - **Área:** frontend
    - **Foco:** {item['focus']}
    - **Tecnologias:** {framework.title()}, TypeScript

    ## Intenção

    Avaliar raciocínio sobre {item['focus']} por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    {chr(10).join(rows)}

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
    """
    for variant, source in (("exercise", broken), ("solution", solution)):
        base = root / variant
        write(base / "package.json", json.dumps(package, ensure_ascii=False, indent=2))
        write(base / "package-lock.json", lockfile(name, framework))
        write(base / ".node-version", "24.15.0")
        write(base / ".gitignore", "node_modules/\ndist/\n.coverage/")
        write(base / "src/challenge.ts", source)
        write(base / component_path, component)
        write(base / "src/styles.css", "body{font-family:system-ui;margin:2rem} main{display:grid;gap:1rem;max-width:48rem} input,button{font:inherit;padding:.5rem}")
        write(base / "tests/public.test.ts", public)
        write(base / "scripts/setup.sh", setup, True)
        write(base / "scripts/start.sh", "#!/usr/bin/env bash\n" + test_script.split("\n", 1)[1].replace("npm test", "node --watch tests/public.test.ts"), True)
        write(base / "scripts/test.sh", test_script, True)
        write(base / "scripts/lint.sh", lint, True)
        write(base / "README.md", readme)
        write(base / "CHALLENGE.md", challenge)
        if variant == "solution":
            write(base / "SOLUTION_NOTES.md", f"# Notas da solução\n\nA referência reduz {item['focus']} a uma política pura com cinco limites verificáveis e mantém o componente como consumidor fino.")
    write(root / "EVALUATION.md", evaluation)
    write(root / "grader/run.py", RUN, True)
    write(root / "grader/hidden.test.ts", "\n".join(hidden))
    write(root / "grader/criteria.json", json.dumps({"exercise": name, "criteria": checks, "staticChecks": []}, ensure_ascii=False, indent=2))


def main() -> None:
    for item in FRONTEND:
        generate(item)
    print(f"Generated {len(FRONTEND)} extended frontend exercises")


if __name__ == "__main__":
    main()
