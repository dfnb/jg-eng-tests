# Avaliação: Fallback de erro

    - **ID:** 68
    - **Área:** frontend
    - **Foco:** resiliência de UI
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre resiliência de UI por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | rede tenta novamente | teste privado `C01` |
| C02 | mínimo | 2 | rede limita retry | teste privado `C02` |
| C03 | mínimo | 2 | auth pede login | teste privado `C03` |
| C04 | intermediário | 2 | render usa fallback | teste privado `C04` |
| C05 | desejado | 1 | fatal usa fallback | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
