# Avaliação: Checkout acessível

- **ID:** 07
- **Nível:** beginner
- **Duração:** 120 minutos
- **Tecnologias:** react, typescript

## Intenção e estado inicial

Avaliar implementação de interface React além do caminho visual feliz.

**Causa/omissão:** validação aceita espaços, payload omite pagamento e componente não tem labels/status.

**Armadilha:** fazer apenas screenshot desktop e ignorar teclado, erro e loading.

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
| C01 | mínimo | 3 | campos vazios ou só com espaços são rejeitados | `C01` |
| C02 | mínimo | 2 | payload normalizado inclui pagamento | `C02` |
| C03 | mínimo | 2 | controles possuem labels associados | `C03` |
| C04 | intermediário | 2 | status é anunciado e submit é bloqueado durante envio | `C04` |
| C05 | desejado | 1 | CSS inclui adaptação móvel | `C05` |

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
