# Desafio: Upload de documentos

## Situação

Proteja contra traversal, tamanho excessivo, tipo forjado e arquivos parciais. Não use o nome do cliente como caminho final.

## Resultado esperado

Leia no máximo `maxBytes+1`, verifique assinatura de conteúdo e grave apenas arquivos aceitos sob `root`.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
