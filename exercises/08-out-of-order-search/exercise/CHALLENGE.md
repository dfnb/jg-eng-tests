# Desafio: Busca fora de ordem

## Situação

Uma resposta antiga substitui a consulta mais recente. Implemente um controlador que publique somente o resultado da geração atual e ignore tudo após dispose.

## Resultado esperado

`SearchController.search` aceita uma função assíncrona; limpar termo publica lista vazia e não chama o transporte.

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
