# Desafio: Importação de catálogo

## Situação

Leia CSV UTF-8 com campos entre aspas, valide SKU único e preço decimal invariável e produza erros com o número da linha, sem persistência parcial.

## Resultado esperado

Implemente `CatalogImporter.Parse`; em qualquer erro, `Items` deve estar vazio e `Errors` deve listar as linhas inválidas.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
