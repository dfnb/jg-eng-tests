# Avaliação: Dashboard lento

- **ID:** 09
- **Nível:** intermediate
- **Duração:** 120 minutos
- **Tecnologias:** angular, typescript

## Intenção e estado inicial

Avaliar performance frontend por trabalho observável, não por milissegundos frágeis.

**Causa/omissão:** a função formata toda a lista e retorna tudo.

**Armadilha:** esconder linhas com CSS ou ordenar mutando o array original.

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
| C01 | mínimo | 3 | janela contém somente size linhas | `C01` |
| C02 | mínimo | 2 | filtro e ordenação são corretos | `C02` |
| C03 | mínimo | 2 | entrada não é mutada | `C03` |
| C04 | intermediário | 2 | formatador roda apenas na janela | `C04` |
| C05 | desejado | 1 | trackBy usa ID | `C05` |

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
