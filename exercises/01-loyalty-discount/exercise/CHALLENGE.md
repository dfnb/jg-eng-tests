# Desafio: Desconto de fidelidade

## Situação

Clientes Silver recebem 5% e clientes Gold 10% de desconto sobre o subtotal antes do imposto. Bronze e níveis desconhecidos não recebem desconto.

## Resultado esperado

Implemente a regra com arredondamento monetário para duas casas, `MidpointRounding.AwayFromZero`, sem confiar em percentuais vindos do cliente.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
