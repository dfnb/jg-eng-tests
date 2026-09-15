#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from production_scale_definitions import BACKEND, FRONTEND

ROOT = Path(__file__).resolve().parents[1]


def entry(item: dict, backend: bool) -> dict:
    return {
        "id": item["id"],
        "slug": item["slug"],
        "title": item["title"],
        "track": "production-backend" if backend else "production-frontend",
        "kind": item["focus"],
        "stack": ["dotnet10"] if backend else [item["framework"], "typescript"],
        "level": "advanced",
        "minutes": 180,
        "status": "ready",
        "codebaseProfile": "small-production",
    }


def docs() -> None:
    plan = """# Plano de expansão 101–130: bases de produção

## Motivação

Os exercícios 101–130 adicionam uma competência deliberadamente ausente nos itens anteriores: navegar, formar um modelo mental e localizar a mudança correta em uma base semelhante a uma aplicação pequena de produção. O defeito ou feature continua focalizado, mas não aparece isolado em um projeto de duas ou três classes.

## Contrato de tamanho

Cada variante de cada exercício desta expansão deve possuir:

- pelo menos 40 arquivos de código de produção;
- pelo menos 800 linhas não vazias em `src/`;
- ao menos seis diretórios funcionais;
- camadas de domínio, aplicação, integração/infraestrutura e entrada pública;
- testes públicos, scripts uniformes, solução, grader e rubrica privada;
- somente uma lacuna deliberada ligada ao desafio.

O validador estrutural mede esses limites. Arquivos repetidos apenas para aumentar contagem não são suficientes: os módulos modelam entidades, repositórios, serviços, estado, adaptadores, utilitários e componentes coerentes com a aplicação simulada.

## Distribuição

| IDs | Área | Quantidade | Temas novos |
| --- | --- | ---: | --- |
| 101–115 | Backend .NET 10 | 15 | aprovação, contabilidade, configuração, histórico, alocação, digest, retenção, rotação, readiness, rollout, shutdown, fan-out, sunset, tracing e deadlocks |
| 116–130 | Frontend | 15 | permissões, undo/redo, autosave, wizard, gráficos acessíveis, movimento reduzido, números locais, identidade, cache, SSR, streaming, quota, clipboard, impressão e microfrontends |

## Estratégia de avaliação

O estudante recebe contexto do produto e comportamento esperado, mas não recebe o caminho do arquivo defeituoso. O grader entra pela API pública da aplicação, atravessando as mesmas fronteiras usadas pelo produto. Cinco critérios binários verificam cada exercício: três mínimos, um intermediário e um desejado.

## Gate de publicação

Todos os 30 itens precisam passar em referência, falhar no mínimo no estado inicial, executar testes públicos e lint/build nas duas variantes, cumprir o perfil de tamanho e gerar pacote sem material privado.
"""
    (ROOT / "docs/EXPANSION_PLAN_130.md").write_text(plan)
    lines = [
        "# Catálogo dos exercícios 101–130",
        "",
        "Todos os itens desta faixa usam o perfil `small-production`; o aluno precisa navegar por uma base ampla antes de alterar o comportamento focal.",
        "",
        "| ID | Exercício | Área | Stack | Competência focal |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in BACKEND + FRONTEND:
        backend = item in BACKEND
        stack = ".NET 10 / C#" if backend else f"{item['framework'].title()} / TypeScript"
        lines.append(f"| {item['id']} | {item['title']} | {'Backend' if backend else 'Frontend'} | {stack} | {item['focus']} |")
    for item in BACKEND + FRONTEND:
        lines += ["", f"## {item['id']} — {item['title']}", "", item["summary"], "", f"- **Foco:** {item['focus']}", "- **Perfil:** pequena aplicação de produção", "- **Critérios discretos:**", ""]
        for index, (description, _input, _expected) in enumerate(item["cases"], 1):
            level = "mínimo" if index <= 3 else "intermediário" if index == 4 else "desejado"
            lines.append(f"  - C{index:02d} ({level}): {description}.")
    (ROOT / "docs/EXERCISES_101_130.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    path = ROOT / "catalog.json"
    catalog = json.loads(path.read_text())
    prior = [item for item in catalog["exercises"] if int(item["id"]) <= 100]
    catalog["exercises"] = prior + [entry(x, True) for x in BACKEND] + [entry(x, False) for x in FRONTEND]
    path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    docs()
    print(f"Catalog expanded to {len(catalog['exercises'])} exercises")


if __name__ == "__main__":
    main()
