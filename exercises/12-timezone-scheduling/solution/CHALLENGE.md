# Desafio: Agendamento e fuso horário

## Situação

Consultas aparecem no dia errado quando o usuário não está em UTC. Calcule a data local e os limites UTC de um dia civil no fuso escolhido.

## Resultado esperado

Use `TimeZoneInfo` e preserve instantes; não dependa do fuso configurado na máquina.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
