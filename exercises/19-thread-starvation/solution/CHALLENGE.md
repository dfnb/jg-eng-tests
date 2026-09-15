# Desafio: API com starvation

## Situação

Sob carga, o serviço bloqueia threads e ignora cancelamento. Faça I/O realmente assíncrono e limite chamadas simultâneas ao orçamento configurado.

## Resultado esperado

`FetchAllAsync` preserva a ordem de IDs, propaga cancelamento e nunca ultrapassa `maxConcurrency`.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
