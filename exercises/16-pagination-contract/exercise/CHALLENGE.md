# Desafio: Contrato de paginação

## Situação

Itens com a mesma data são repetidos ou omitidos entre páginas. Implemente ordenação `(CreatedAt desc, Id asc)` e cursor exclusivo sobre os dois campos.

## Resultado esperado

`Page` deve retornar no máximo `take` itens, rejeitar limites inválidos e manter continuidade determinística.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
