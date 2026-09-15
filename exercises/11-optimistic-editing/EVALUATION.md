# Avaliação: Edição otimista

- **ID:** 11
- **Nível:** intermediate
- **Duração:** 120 minutos
- **Tecnologias:** react, typescript

## Intenção e estado inicial

Avaliar estado otimista, rollback condicional e conflito de integração.

**Causa/omissão:** qualquer falha restaura um snapshot antigo, apagando edição posterior.

**Armadilha:** rollback cego ou tratar HTTP 409 como erro genérico.

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
| C01 | mínimo | 3 | valor é publicado antes da resposta | `C01` |
| C02 | mínimo | 2 | falha simples reverte | `C02` |
| C03 | mínimo | 2 | rollback antigo não apaga edição nova | `C03` |
| C04 | intermediário | 2 | conflito retorna estado próprio | `C04` |
| C05 | desejado | 1 | componente anuncia o resultado | `C05` |

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
