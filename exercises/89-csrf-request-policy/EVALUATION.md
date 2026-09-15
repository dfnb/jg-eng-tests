# Avaliação: Envio de CSRF

    - **ID:** 89
    - **Área:** frontend
    - **Foco:** segurança
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre segurança por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | POST local recebe token | teste privado `C01` |
| C02 | mínimo | 2 | GET não recebe | teste privado `C02` |
| C03 | mínimo | 2 | origem externa não recebe | teste privado `C03` |
| C04 | intermediário | 2 | token ausente não inventa | teste privado `C04` |
| C05 | desejado | 1 | DELETE local recebe | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
