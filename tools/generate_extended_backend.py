#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

from extended_definitions import BACKEND
from generate_dotnet_exercises import GRADER

ROOT = Path(__file__).resolve().parents[1]


def clean(value: str) -> str:
    return dedent(value).strip() + "\n"


def write(path: Path, value: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(value))
    if executable:
        path.chmod(0o755)


def csharp(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def generate(item: dict) -> None:
    name = f"{item['id']}-{item['slug']}"
    root = ROOT / "exercises" / name
    project = """
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <TargetFramework>net10.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
        <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
      </PropertyGroup>
    </Project>
    """
    test_project = """
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net10.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup>
      <ItemGroup><ProjectReference Include="../../src/Challenge/Challenge.csproj" /></ItemGroup>
    </Project>
    """
    header = """using System.Globalization;
    using System.Text;
    using System.Text.RegularExpressions;

    namespace Challenge;

    public static class Policy
    {
        public static string Evaluate(string input)
        {
    """
    footer = """
        }
    }
    """
    broken = header + '        return "<unimplemented>";' + footer
    solution = header + "        " + item["body"] + footer
    public = f"""using Challenge;
    var output = Policy.Evaluate({csharp(item['cases'][0][1])});
    if (output is null) throw new Exception("O contrato não pode retornar null.");
    Console.WriteLine("public-tests: ok");
    """
    checks = []
    hidden = [
        "using Challenge;",
        "static void Check(string id, Func<bool> test)",
        "{",
        "    try { Console.WriteLine($\"{id}|{(test() ? \"pass\" : \"fail\")}\"); }",
        "    catch (Exception error) { Console.WriteLine($\"{id}|fail|{error.GetType().Name}\"); }",
        "}",
    ]
    for index, (description, input_value, expected) in enumerate(item["cases"], 1):
        criterion = f"C{index:02d}"
        hidden.append(f"Check(\"{criterion}\", () => Policy.Evaluate({csharp(input_value)}) == {csharp(expected)});")
        checks.append({
            "id": criterion,
            "level": "minimum" if index <= 3 else "intermediate" if index == 4 else "desired",
            "weight": 3 if index == 1 else 2 if index <= 4 else 1,
            "description": description,
        })
    setup = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    command -v dotnet >/dev/null || { echo "Instale o SDK .NET 10." >&2; exit 1; }
    dotnet restore "$root/tests/PublicTests/PublicTests.csproj" --nologo
    """
    test = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    dotnet run --project "$root/tests/PublicTests/PublicTests.csproj" --nologo
    """
    lint = """#!/usr/bin/env bash
    set -euo pipefail
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    dotnet build "$root/tests/PublicTests/PublicTests.csproj" --nologo --no-restore
    """
    readme = f"""# {item['title']}

    Este repositório simula um componente de uma aplicação empresarial. A regra isolada representa uma decisão encontrada em produção e usa texto como formato de fixture para manter o exercício autocontido.

    ## Stack e arquitetura

    C# com .NET 10. A API pública está em `src/Challenge/Challenge.cs`; os testes públicos verificam apenas o contrato básico.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    Não são necessárias credenciais, banco de dados ou conexão de rede.
    """
    challenge = f"""# Desafio: {item['title']}

    ## Contexto

    {item['summary']}

    ## Pedido

    Complete `Policy.Evaluate` de acordo com o contrato descrito pelo domínio e preserve a assinatura pública. Investigue os casos de borda coerentes com **{item['focus']}** e acrescente testes de regressão quando necessário.

    ## Restrições

    A solução deve ser determinística, funcionar para entradas equivalentes além dos exemplos públicos e permanecer compatível com .NET 10. Não adicione dependências ou serviços externos.

    ## Verificação

    Execute `./scripts/test.sh` e `./scripts/lint.sh`. Os testes de avaliação cobrem situações adicionais que não são reveladas no repositório do estudante.
    """
    rows = []
    for check in checks:
        level = {"minimum": "mínimo", "intermediate": "intermediário", "desired": "desejado"}[check["level"]]
        rows.append(f"| {check['id']} | {level} | {check['weight']} | {check['description']} | teste privado `{check['id']}` |")
    evaluation = f"""# Avaliação: {item['title']}

    - **ID:** {item['id']}
    - **Área:** backend
    - **Foco:** {item['focus']}
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de {item['focus']} em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    {chr(10).join(rows)}

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
    """
    for variant, source in (("exercise", broken), ("solution", solution)):
        base = root / variant
        write(base / "global.json", '{"sdk":{"version":"10.0.100","rollForward":"latestFeature"}}')
        write(base / ".gitignore", "bin/\nobj/\n*.user\n.idea/\n.vscode/")
        write(base / "src/Challenge/Challenge.csproj", project)
        write(base / "src/Challenge/Challenge.cs", source)
        write(base / "tests/PublicTests/PublicTests.csproj", test_project)
        write(base / "tests/PublicTests/Program.cs", public)
        write(base / "scripts/setup.sh", setup, True)
        write(base / "scripts/start.sh", test, True)
        write(base / "scripts/test.sh", test, True)
        write(base / "scripts/lint.sh", lint, True)
        write(base / "README.md", readme)
        write(base / "CHALLENGE.md", challenge)
        if variant == "solution":
            write(base / "SOLUTION_NOTES.md", f"# Notas da solução\n\nA referência implementa os cinco limites observáveis de {item['focus']} em uma função pura para manter o feedback determinístico.")
    write(root / "EVALUATION.md", evaluation)
    write(root / "grader/run.py", GRADER, True)
    write(root / "grader/Program.cs", "\n".join(hidden))
    spec = {"exercise": name, "criteria": checks, "staticChecks": []}
    write(root / "grader/criteria.json", json.dumps(spec, ensure_ascii=False, indent=2))


def main() -> None:
    for item in BACKEND:
        generate(item)
    print(f"Generated {len(BACKEND)} extended backend exercises")


if __name__ == "__main__":
    main()
