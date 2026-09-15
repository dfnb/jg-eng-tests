# Pagamento resiliente

Este repositório simula um cliente de pagamentos com provedor fake. Resultados são `Success`, `Transient` ou `Permanent`.

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
