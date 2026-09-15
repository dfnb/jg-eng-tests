# Desafio: Checkout modular

## Situação

O checkout deve validar o carrinho, reservar estoque, cobrar e confirmar o pedido. Falha de pagamento libera a reserva e nunca confirma o pedido.

## Resultado esperado

Organize a orquestração em torno das interfaces fornecidas e preserve a regra de compensação.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
