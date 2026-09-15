# Avaliação: Closure obsoleta

    - **ID:** 78
    - **Área:** frontend
    - **Foco:** estado assíncrono
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre estado assíncrono por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | dois ticks acumulam | teste privado `C01` |
| C02 | mínimo | 2 | parte de valor atual | teste privado `C02` |
| C03 | mínimo | 2 | delta negativo | teste privado `C03` |
| C04 | intermediário | 2 | nenhum tick preserva | teste privado `C04` |
| C05 | desejado | 1 | muitos ticks | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
