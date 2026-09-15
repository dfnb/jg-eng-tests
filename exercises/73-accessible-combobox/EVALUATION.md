# Avaliação: Combobox acessível

    - **ID:** 73
    - **Área:** frontend
    - **Foco:** acessibilidade
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre acessibilidade por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | filtra sem caixa | teste privado `C01` |
| C02 | mínimo | 2 | active inválido muda | teste privado `C02` |
| C03 | mínimo | 2 | sem resultado limpa active | teste privado `C03` |
| C04 | intermediário | 2 | vazio mantém active | teste privado `C04` |
| C05 | desejado | 1 | primeira opção vira active | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
