# Avaliação: Busca fora de ordem

- **ID:** 08
- **Nível:** intermediate
- **Duração:** 90 minutos
- **Tecnologias:** react, typescript

## Intenção e estado inicial

Avaliar race condition no cliente e ciclo de vida assíncrono.

**Causa/omissão:** toda promessa atualiza o estado quando termina.

**Armadilha:** aumentar debounce sem garantir ordem.

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
| C01 | mínimo | 3 | só a busca mais recente publica | `C01` |
| C02 | mínimo | 2 | termo vazio limpa sem chamar API | `C02` |
| C03 | mínimo | 2 | dispose impede publicação tardia | `C03` |
| C04 | intermediário | 2 | erro obsoleto não apaga resultado novo | `C04` |
| C05 | desejado | 1 | componente limpa controller ao desmontar | `C05` |

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
