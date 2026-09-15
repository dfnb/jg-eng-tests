# Avaliação: Reordenação por teclado

    - **ID:** 74
    - **Área:** frontend
    - **Foco:** acessibilidade
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre acessibilidade por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | move para cima | teste privado `C01` |
| C02 | mínimo | 2 | move para baixo | teste privado `C02` |
| C03 | mínimo | 2 | topo não sai | teste privado `C03` |
| C04 | intermediário | 2 | fim não sai | teste privado `C04` |
| C05 | desejado | 1 | ID ausente não muda | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
