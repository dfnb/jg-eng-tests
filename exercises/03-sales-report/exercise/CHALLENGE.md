# Desafio: Relatório de vendas

## Situação

Produza receita e quantidade por produto em um intervalo semiaberto `[from, to)`, excluindo vendas canceladas, ordenando por receita decrescente e ID como desempate, e só então paginando.

## Resultado esperado

Corrija a consulta preservando uma ordenação determinística e validação de paginação.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
