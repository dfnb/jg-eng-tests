# Plano de expansão para 100 exercícios

## Objetivo

Ampliar a coleção de 30 para 100 exercícios sem repetir o núcleo dos desafios existentes. A expansão adiciona 35 exercícios de backend e 35 de frontend. Cada item mantém o mesmo contrato editorial: repositório autocontido do estudante, solução de referência, grader privado e rubrica discreta.

## Distribuição

| Faixa | Trilha | Lacunas cobertas |
| --- | --- | --- |
| 31–40 | Backend: contratos HTTP e APIs | negociação de conteúdo, ETag, idempotência, rate limit, cursores e compatibilidade |
| 41–48 | Backend: identidade e segurança | escopos, tokens, redaction, traversal, SSRF, CORS, limites e igualdade temporal |
| 49–55 | Backend: dados e cache | ordenação, Unicode, datas, cache-aside, stampede, jitter e invalidação |
| 56–65 | Backend: sistemas distribuídos | circuit breaker, retry, outbox, DLQ, saga, leases, relógios e versionamento |
| 66–75 | Frontend: navegação, formulários e acessibilidade | roteamento, filtros, uploads, foco, teclado e localização |
| 76–85 | Frontend: estado, tempo real e performance | seletores, WebSocket, cache, polling, listas e recursos assíncronos |
| 86–95 | Frontend: offline, segurança e ciclo de vida | service workers, XSS, CSRF, CSP, URLs, supply chain e cleanup |
| 96–100 | Frontend: processamento e arquitetura | workers, colaboração, temas, testes determinísticos e design system |

## Estratégia de implementação

1. Registrar os 70 itens no catálogo com ID, stack, dificuldade e duração.
2. Gerar uma base executável por exercício, sem dependências externas ou credenciais.
3. Manter cinco critérios binários por item: três mínimos, um intermediário e um desejado.
4. Fazer o estado inicial compilar e passar nos testes públicos, mas falhar no mínimo privado.
5. Executar grader, auditoria do estado inicial, testes públicos, lint/build e empacotamento.

## Critério de conclusão

A expansão só é considerada concluída quando os 100 diretórios existem, as 100 referências passam, os 100 estados iniciais continuam incompletos, e todos podem ser empacotados sem conteúdo privado.
