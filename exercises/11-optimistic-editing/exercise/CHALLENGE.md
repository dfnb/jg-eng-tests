# Desafio: Edição otimista

## Situação

Aplique edição imediatamente; em falha reverta somente se nenhuma edição mais nova substituiu aquela versão. Conflito deve ser distinguido de falha comum.

## Resultado esperado

`OptimisticStore.edit` retorna `ok`, `failed` ou `conflict` e mantém o estado mais recente sob mutações sobrepostas.

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
