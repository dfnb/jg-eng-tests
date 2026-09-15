# Desafio: Pagamento resiliente

## Situação

Repita somente falhas transitórias, no máximo três tentativas, sempre com a mesma chave idempotente. Cancelamento deve parar imediatamente e falhas consecutivas devem abrir o breaker da instância.

## Resultado esperado

Depois de duas operações esgotadas, uma terceira retorna `CircuitOpen` sem chamar o provedor.

## Restrições

Preserve as APIs públicas e o comportamento já coberto. A solução deve ser determinística, não pode codificar apenas os exemplos públicos e deve permanecer compatível com .NET 10.

## Fora de escopo

Interface gráfica, autenticação real e provisionamento de nuvem não fazem parte deste desafio.

## Verificação e entrega

Execute `./scripts/test.sh` e `./scripts/lint.sh`. Entregue o repositório completo com testes de regressão que considerar relevantes.
