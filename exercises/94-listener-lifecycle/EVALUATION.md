# Avaliação: Ciclo de listeners

    - **ID:** 94
    - **Área:** frontend
    - **Foco:** memory leaks
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre memory leaks por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | monta/desmonta limpa | teste privado `C01` |
| C02 | mínimo | 2 | montagem sem cleanup vaza | teste privado `C02` |
| C03 | mínimo | 2 | duas instâncias limpas | teste privado `C03` |
| C04 | intermediário | 2 | cleanup extra inválido | teste privado `C04` |
| C05 | desejado | 1 | uma sobra detecta | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
