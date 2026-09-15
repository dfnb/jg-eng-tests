# Avaliação: Nonce de CSP

    - **ID:** 90
    - **Área:** frontend
    - **Foco:** segurança
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre segurança por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | script confiável recebe nonce | teste privado `C01` |
| C02 | mínimo | 2 | não confiável bloqueia | teste privado `C02` |
| C03 | mínimo | 2 | nonce ausente bloqueia | teste privado `C03` |
| C04 | intermediário | 2 | valor é preservado | teste privado `C04` |
| C05 | desejado | 1 | não inventa nonce | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
