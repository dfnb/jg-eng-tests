# Avaliação: Upcasting de eventos

    - **ID:** 53
    - **Área:** backend
    - **Foco:** compatibilidade de schema
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de compatibilidade de schema em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | v1 recebe default | teste privado `C01` |
| C02 | mínimo | 2 | v2 preserva moeda | teste privado `C02` |
| C03 | mínimo | 2 | v3 não muda | teste privado `C03` |
| C04 | intermediário | 2 | texto Unicode preserva | teste privado `C04` |
| C05 | desejado | 1 | default é determinístico | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
