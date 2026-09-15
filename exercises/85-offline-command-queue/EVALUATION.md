# Avaliação: Fila offline

    - **ID:** 85
    - **Área:** frontend
    - **Foco:** offline-first
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre offline-first por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | updates compactam | teste privado `C01` |
| C02 | mínimo | 2 | delete vence update anterior | teste privado `C02` |
| C03 | mínimo | 2 | update não ressuscita delete | teste privado `C03` |
| C04 | intermediário | 2 | IDs distintos permanecem | teste privado `C04` |
| C05 | desejado | 1 | vazio | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
