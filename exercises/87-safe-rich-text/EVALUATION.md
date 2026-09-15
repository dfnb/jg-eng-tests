# Avaliação: Texto rico seguro

    - **ID:** 87
    - **Área:** frontend
    - **Foco:** segurança XSS
    - **Tecnologias:** Angular, TypeScript

    ## Intenção

    Avaliar raciocínio sobre segurança XSS por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | script vira texto | teste privado `C01` |
| C02 | mínimo | 2 | ampersand escapa | teste privado `C02` |
| C03 | mínimo | 2 | aspas escapam | teste privado `C03` |
| C04 | intermediário | 2 | apóstrofo escapa | teste privado `C04` |
| C05 | desejado | 1 | Unicode permanece | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
