# Avaliação: Teste de UI determinístico

    - **ID:** 100
    - **Área:** frontend
    - **Foco:** qualidade de testes
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre qualidade de testes por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | evento pronto passa | teste privado `C01` |
| C02 | mínimo | 2 | poll pronto passa | teste privado `C02` |
| C03 | mínimo | 2 | sleep é frágil | teste privado `C03` |
| C04 | intermediário | 2 | estado incompleto não passa | teste privado `C04` |
| C05 | desejado | 1 | timeout fixo continua frágil | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
