# Avaliação: Rotas lazy

    - **ID:** 92
    - **Área:** frontend
    - **Foco:** bundle size
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre bundle size por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | admin lazy está correto | teste privado `C01` |
| C02 | mínimo | 2 | admin eager viola | teste privado `C02` |
| C03 | mínimo | 2 | subrota admin também | teste privado `C03` |
| C04 | intermediário | 2 | home pode ser eager | teste privado `C04` |
| C05 | desejado | 1 | login eager é aceitável | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
