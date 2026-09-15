# Avaliação: Versão de cache offline

    - **ID:** 86
    - **Área:** frontend
    - **Foco:** service worker
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre service worker por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | remove versão anterior | teste privado `C01` |
| C02 | mínimo | 2 | preserva outro app | teste privado `C02` |
| C03 | mínimo | 2 | remove múltiplas antigas | teste privado `C03` |
| C04 | intermediário | 2 | sem caches | teste privado `C04` |
| C05 | desejado | 1 | não remove atual | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
