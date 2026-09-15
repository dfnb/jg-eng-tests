# Avaliação: Particionamento para Web Worker

    - **ID:** 96
    - **Área:** frontend
    - **Foco:** performance CPU
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre performance CPU por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | divide igualmente | teste privado `C01` |
| C02 | mínimo | 2 | distribui resto | teste privado `C02` |
| C03 | mínimo | 2 | mais workers que itens | teste privado `C03` |
| C04 | intermediário | 2 | zero itens | teste privado `C04` |
| C05 | desejado | 1 | zero workers vira um | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
