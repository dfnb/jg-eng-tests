# Desafio: Motor de preços legado

## Situação

Refatore o motor para aceitar regras substituíveis e testáveis, preservando a ordem recebida e impedindo total negativo.

## Resultado esperado

A adição de uma nova implementação de `IPromotion` não deve exigir alteração no motor.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
