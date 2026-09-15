# Desafio: Reserva de estoque

## Situação

Cancelar uma reserva ativa deve devolver o estoque uma única vez. Hoje o estado da reserva muda, mas o saldo continua reduzido.

## Resultado esperado

Corrija a transição mantendo reserva, cancelamento e repetição consistentes, inclusive quando chamadas concorrentes chegam para a mesma reserva.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
