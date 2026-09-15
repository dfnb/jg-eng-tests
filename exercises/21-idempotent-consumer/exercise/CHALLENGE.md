# Desafio: Consumidor idempotente

## Situação

A mesma chave de mensagem deve produzir uma única fatura. Se ocorrer falha antes do commit lógico, a nova entrega deve poder concluir sem duplicação.

## Resultado esperado

A deduplicação deve residir no armazenamento compartilhado e efeito/marcação devem ser atômicos no modelo fornecido.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
