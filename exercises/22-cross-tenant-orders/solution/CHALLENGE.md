# Desafio: Pedidos de outro cliente

## Situação

Usuários conseguem ler, alterar ou cancelar pedidos de outro cliente ao trocar o ID. Aplique autorização por recurso em todas as operações.

## Resultado esperado

Somente o proprietário pode operar; a resposta para recurso inexistente ou alheio deve seguir a política `NotFound`.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
