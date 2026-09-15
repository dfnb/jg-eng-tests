# Desafio: Serviço de encurtamento

## Situação

Implemente criação e resolução. Aceite somente HTTP/HTTPS absolutos, trate colisões tentando outro código e garanta unicidade com instâncias que compartilham a store.

## Resultado esperado

Códigos já existentes não podem ser sobrescritos; `Resolve` retorna null quando ausente.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
