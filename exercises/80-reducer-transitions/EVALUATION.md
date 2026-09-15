# Avaliação: Reducer de fluxo

    - **ID:** 80
    - **Área:** frontend
    - **Foco:** arquitetura frontend
    - **Tecnologias:** React, TypeScript

    ## Intenção

    Avaliar raciocínio sobre arquitetura frontend por propriedades observáveis e determinísticas, sem depender de screenshots ou tempo de máquina.

    **Omissão deliberada:** a função inicial mantém o contrato exportado, mas não implementa a política.

    **Armadilha:** tratar apenas a aparência ou o fixture público e ignorar estados menos comuns.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | submit inicia envio | teste privado `C01` |
| C02 | mínimo | 2 | sucesso conclui | teste privado `C02` |
| C03 | mínimo | 2 | falha retorna edição | teste privado `C03` |
| C04 | intermediário | 2 | reset reabre | teste privado `C04` |
| C05 | desejado | 1 | evento inválido preserva | teste privado `C05` |

    São aceitas implementações diferentes da referência quando preservam a exportação e cumprem os resultados observáveis.
