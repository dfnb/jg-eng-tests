# Avaliação: Estados de carregamento

    - **ID:** 69
    - **Área:** frontend
    - **Foco:** estado de UI
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre estado de UI por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | loading atrasado aparece | teste privado `C01` |
| C02 | mínimo | 2 | loading curto não pisca | teste privado `C02` |
| C03 | mínimo | 2 | zero itens é vazio | teste privado `C03` |
| C04 | intermediário | 2 | itens são sucesso | teste privado `C04` |
| C05 | desejado | 1 | erro prevalece | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
