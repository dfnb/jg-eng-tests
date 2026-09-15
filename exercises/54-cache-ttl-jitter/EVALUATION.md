# Avaliação: Jitter de cache

    - **ID:** 54
    - **Área:** backend
    - **Foco:** cache
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de cache em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | mesma chave é estável | teste privado `C01` |
| C02 | mínimo | 2 | outra chave varia | teste privado `C02` |
| C03 | mínimo | 2 | jitter fica pequeno | teste privado `C03` |
| C04 | intermediário | 2 | base é respeitada | teste privado `C04` |
| C05 | desejado | 1 | Unicode é determinístico | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
