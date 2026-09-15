# Desafio: Canais de notificação

## Situação

Envie a mensagem por todos os canais preferidos registrados. Canal desconhecido é ignorado e falha de um canal não impede os demais.

## Resultado esperado

Remova condicionais específicas de provedor do orquestrador e use as abstrações fornecidas para tornar novos canais registráveis.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
