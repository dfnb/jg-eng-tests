# Desafio: Checkout acessível

## Situação

Complete validação, payload e estados acessíveis de uma tela de checkout. Nome, endereço e método de pagamento são obrigatórios.

## Resultado esperado

`validateCheckout` produz erros por campo; `buildOrder` normaliza texto sem descartar o método; o componente associa labels/erros, bloqueia duplo envio e anuncia status.

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
