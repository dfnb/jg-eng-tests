# Desafio: Exportação sem memória

## Situação

Produza linhas progressivamente: antes do primeiro `yield`, no máximo um item pode ter sido lido. Propague cancelamento e faça escaping CSV.

## Resultado esperado

`Export` deve permanecer um `IAsyncEnumerable<string>` e não acumular o conjunto completo.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
