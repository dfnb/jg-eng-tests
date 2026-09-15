# Desafio: Formulário por esquema

## Situação

Converta os campos suportados (`text`, `number`, `select`) em um modelo tipado, valide obrigatoriedade/min/max e rejeite esquema desconhecido.

## Resultado esperado

`buildForm` devolve valores com tipos corretos, erros por campo e `valid` global; não codifique nomes dos fixtures.

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
