# Avaliação: Pluralização de mensagens

    - **ID:** 70
    - **Área:** frontend
    - **Foco:** i18n
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre i18n por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | pt singular | teste privado `C01` |
| C02 | mínimo | 2 | pt plural | teste privado `C02` |
| C03 | mínimo | 2 | pt zero plural | teste privado `C03` |
| C04 | intermediário | 2 | en singular | teste privado `C04` |
| C05 | desejado | 1 | en plural | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
