# Avaliação: Imagem responsiva

    - **ID:** 93
    - **Área:** frontend
    - **Foco:** performance web
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre performance web por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | viewport simples | teste privado `C01` |
| C02 | mínimo | 2 | DPR dois dobra alvo | teste privado `C02` |
| C03 | mínimo | 2 | menor suficiente | teste privado `C03` |
| C04 | intermediário | 2 | alvo maior usa máximo | teste privado `C04` |
| C05 | desejado | 1 | entrada desordenada funciona | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
