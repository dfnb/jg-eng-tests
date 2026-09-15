# Desafio: Totais monetários

## Situação

Totais divergem por centavos. Elimine ponto flutuante binário e implemente arredondamento monetário `AwayFromZero` nos limites descritos.

## Resultado esperado

`Invoice.Total` deve ser simétrico para estornos e produzir duas casas decimais.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
