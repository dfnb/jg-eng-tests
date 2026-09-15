# Avaliação: Imports tree-shakable

    - **ID:** 91
    - **Área:** frontend
    - **Foco:** bundle size
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre bundle size por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | submódulo é granular | teste privado `C01` |
| C02 | mínimo | 2 | pacote inteiro é pesado | teste privado `C02` |
| C03 | mínimo | 2 | barrel all é pesado | teste privado `C03` |
| C04 | intermediário | 2 | arquivo index é pesado | teste privado `C04` |
| C05 | desejado | 1 | função direta é granular | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
