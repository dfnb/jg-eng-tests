# Desafio: Recebimento de webhooks

## Situação

Valide a assinatura em tempo constante e processe cada `id` JSON apenas uma vez.

## Resultado esperado

Corpo alterado ou assinatura inválida é rejeitado; repetição válida responde sucesso idempotente sem novo efeito.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
