# Desafio: Cupons concorrentes

## Situação

Requisições simultâneas conseguem confirmar o mesmo cupom. Faça a verificação e a gravação atômicas no estado compartilhado.

## Resultado esperado

Exatamente um resgate retorna sucesso e auditoria/saldo permanecem consistentes.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
