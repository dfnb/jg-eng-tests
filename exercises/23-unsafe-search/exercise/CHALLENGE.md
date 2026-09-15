# Desafio: Busca vulnerável

## Situação

Elimine injeção em filtro e ordenação. Valores devem ser parametrizados; coluna e direção só podem vir de allowlists.

## Resultado esperado

Campos permitidos são `name`, `createdAt`; direções `asc`, `desc`. Entrada inválida gera `ArgumentException`.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
