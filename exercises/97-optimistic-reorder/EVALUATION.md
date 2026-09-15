# Avaliação: Reordenação otimista

    - **ID:** 97
    - **Área:** frontend
    - **Foco:** estado otimista
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre estado otimista por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | move antes de item | teste privado `C01` |
| C02 | mínimo | 2 | move ao fim | teste privado `C02` |
| C03 | mínimo | 2 | estado novo preserva item novo | teste privado `C03` |
| C04 | intermediário | 2 | ID ausente é inserido | teste privado `C04` |
| C05 | desejado | 1 | alvo ausente vai ao início | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
