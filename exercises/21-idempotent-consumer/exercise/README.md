# Consumidor idempotente

Este repositório simula um consumidor de eventos de faturamento sujeito a redelivery e execução por duas instâncias.

## Arquitetura

A regra avaliada fica em `src/Challenge`. `tests/PublicTests` contém somente testes básicos do contrato; a avaliação usa casos adicionais. Não altere assinaturas públicas sem necessidade.

## Pré-requisitos

- SDK .NET 10
- Bash para os atalhos em `scripts/`

## Executar

```bash
./scripts/setup.sh
./scripts/test.sh
./scripts/lint.sh
```

O projeto não usa serviços pagos, credenciais nem acesso à internet durante os testes.
