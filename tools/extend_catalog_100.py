#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from extended_definitions import BACKEND, FRONTEND

ROOT = Path(__file__).resolve().parents[1]


def catalog_item(item: dict, backend: bool) -> dict:
    number = int(item["id"])
    if backend:
        if number <= 40:
            track = "api-contracts"
        elif number <= 48:
            track = "backend-security"
        elif number <= 55:
            track = "data-cache"
        else:
            track = "resilience-distributed"
        stack = ["dotnet10"]
        if item["focus"] in {"consulta", "dados temporais"}:
            stack.append("linq")
    else:
        track = "frontend-advanced"
        stack = [item["framework"], "typescript"]
    return {
        "id": item["id"],
        "slug": item["slug"],
        "title": item["title"],
        "track": track,
        "kind": item["focus"],
        "stack": stack,
        "level": "advanced" if number in range(56, 66) else "intermediate",
        "minutes": 90 if number < 56 or number >= 66 else 120,
        "status": "ready",
    }


def write_docs() -> None:
    groups = [
        ("31–40", "Backend: contratos HTTP e APIs", "negociação de conteúdo, ETag, idempotência, rate limit, cursores e compatibilidade"),
        ("41–48", "Backend: identidade e segurança", "escopos, tokens, redaction, traversal, SSRF, CORS, limites e igualdade temporal"),
        ("49–55", "Backend: dados e cache", "ordenação, Unicode, datas, cache-aside, stampede, jitter e invalidação"),
        ("56–65", "Backend: sistemas distribuídos", "circuit breaker, retry, outbox, DLQ, saga, leases, relógios e versionamento"),
        ("66–75", "Frontend: navegação, formulários e acessibilidade", "roteamento, filtros, uploads, foco, teclado e localização"),
        ("76–85", "Frontend: estado, tempo real e performance", "seletores, WebSocket, cache, polling, listas e recursos assíncronos"),
        ("86–95", "Frontend: offline, segurança e ciclo de vida", "service workers, XSS, CSRF, CSP, URLs, supply chain e cleanup"),
        ("96–100", "Frontend: processamento e arquitetura", "workers, colaboração, temas, testes determinísticos e design system"),
    ]
    plan = """# Plano de expansão para 100 exercícios

## Objetivo

Ampliar a coleção de 30 para 100 exercícios sem repetir o núcleo dos desafios existentes. A expansão adiciona 35 exercícios de backend e 35 de frontend. Cada item mantém o mesmo contrato editorial: repositório autocontido do estudante, solução de referência, grader privado e rubrica discreta.

## Distribuição

| Faixa | Trilha | Lacunas cobertas |
| --- | --- | --- |
"""
    plan += "\n".join(f"| {span} | {title} | {focus} |" for span, title, focus in groups)
    plan += """

## Estratégia de implementação

1. Registrar os 70 itens no catálogo com ID, stack, dificuldade e duração.
2. Gerar uma base executável por exercício, sem dependências externas ou credenciais.
3. Manter cinco critérios binários por item: três mínimos, um intermediário e um desejado.
4. Fazer o estado inicial compilar e passar nos testes públicos, mas falhar no mínimo privado.
5. Executar grader, auditoria do estado inicial, testes públicos, lint/build e empacotamento.

## Critério de conclusão

A expansão só é considerada concluída quando os 100 diretórios existem, as 100 referências passam, os 100 estados iniciais continuam incompletos, e todos podem ser empacotados sem conteúdo privado.
"""
    (ROOT / "docs/EXPANSION_PLAN_100.md").write_text(plan)

    lines = [
        "# Catálogo dos exercícios 31–100",
        "",
        "Este documento detalha a expansão planejada. Os cinco critérios de cada exercício são observáveis pelo grader; C01–C03 formam o mínimo, C04 é intermediário e C05 é desejado.",
        "",
        "| ID | Exercício | Área | Tecnologia | Foco |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in BACKEND + FRONTEND:
        area = "Backend" if item in BACKEND else "Frontend"
        tech = ".NET 10 / C#" if area == "Backend" else f"{item['framework'].title()} / TypeScript"
        lines.append(f"| {item['id']} | {item['title']} | {area} | {tech} | {item['focus']} |")
    for item in BACKEND + FRONTEND:
        area = "Backend (.NET 10)" if item in BACKEND else f"Frontend ({item['framework'].title()} + TypeScript)"
        lines += [
            "",
            f"## {item['id']} — {item['title']}",
            "",
            f"- **Área:** {area}",
            f"- **Foco:** {item['focus']}",
            f"- **Problema:** {item['summary']}",
            "- **Critérios discretos:**",
            "",
        ]
        for index, (description, _input, _expected) in enumerate(item["cases"], 1):
            level = "mínimo" if index <= 3 else "intermediário" if index == 4 else "desejado"
            lines.append(f"  - C{index:02d} ({level}): {description}.")
    (ROOT / "docs/EXERCISES_31_100.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    path = ROOT / "catalog.json"
    catalog = json.loads(path.read_text())
    original = [item for item in catalog["exercises"] if int(item["id"]) <= 30]
    additions = [catalog_item(item, True) for item in BACKEND]
    additions += [catalog_item(item, False) for item in FRONTEND]
    catalog["exercises"] = original + additions
    path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
    write_docs()
    print(f"Catalog and plan updated: {len(catalog['exercises'])} exercises")


if __name__ == "__main__":
    main()
