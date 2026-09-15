# Avaliação: Data no fuso do usuário

    - **ID:** 71
    - **Área:** frontend
    - **Foco:** datas
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre datas por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | offset cruza para ontem | teste privado `C01` |
| C02 | mínimo | 2 | UTC preserva dia | teste privado `C02` |
| C03 | mínimo | 2 | offset cruza amanhã | teste privado `C03` |
| C04 | intermediário | 2 | meia-noite local | teste privado `C04` |
| C05 | desejado | 1 | ano novo local | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
