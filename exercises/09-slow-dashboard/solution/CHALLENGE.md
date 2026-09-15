# Desafio: Dashboard lento

## Situação

`visibleRows` hoje ordena/mapeia todo o conjunto antes de filtrar e ignora a janela. Retorne somente a fatia visível depois do filtro e uma ordenação estável sem mutar a entrada.

## Resultado esperado

Respeite `start` e `size`, preserve seleção por ID e não execute o formatador em linhas fora da janela.

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
