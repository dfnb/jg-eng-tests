# Avaliação: Dependências de memoização

    - **ID:** 77
    - **Área:** frontend
    - **Foco:** performance
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre performance por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | inclui usuário | teste privado `C01` |
| C02 | mínimo | 2 | inclui locale | teste privado `C02` |
| C03 | mínimo | 2 | ordem de itens estabiliza | teste privado `C03` |
| C04 | intermediário | 2 | lista vazia | teste privado `C04` |
| C05 | desejado | 1 | usuários não colidem | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
