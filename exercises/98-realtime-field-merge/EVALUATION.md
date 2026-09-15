# Avaliação: Merge em tempo real

    - **ID:** 98
    - **Área:** frontend
    - **Foco:** colaboração
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre colaboração por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | só remoto muda | teste privado `C01` |
| C02 | mínimo | 2 | só local muda | teste privado `C02` |
| C03 | mínimo | 2 | mudanças iguais mesclam | teste privado `C03` |
| C04 | intermediário | 2 | mudanças diferentes conflitam | teste privado `C04` |
| C05 | desejado | 1 | nenhuma mudança usa merged | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
