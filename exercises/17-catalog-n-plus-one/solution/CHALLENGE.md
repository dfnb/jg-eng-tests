# Desafio: Catálogo N+1

## Situação

Eliminar o padrão N+1: `CatalogService.List` deve carregar produtos e disponibilidades em no máximo duas consultas, mantendo paginação e valores.

## Resultado esperado

Use a operação em lote do repositório e não um cache global.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
