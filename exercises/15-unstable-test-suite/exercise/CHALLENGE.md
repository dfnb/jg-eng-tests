# Desafio: Suíte de testes instável

## Situação

Torne `TokenService` determinístico e seguro para testes paralelos usando as abstrações já fornecidas.

## Resultado esperado

O prazo deve vir de `IClock`, o nonce de `INonceSource` e chamadas concorrentes não podem compartilhar estado mutável.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
