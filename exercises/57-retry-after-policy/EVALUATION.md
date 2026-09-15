# Avaliação: Retry-After

    - **ID:** 57
    - **Área:** backend
    - **Foco:** resiliência HTTP
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de resiliência HTTP em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | delta válido | teste privado `C01` |
| C02 | mínimo | 2 | espera é limitada | teste privado `C02` |
| C03 | mínimo | 2 | zero é válido | teste privado `C03` |
| C04 | intermediário | 2 | negativo é inválido | teste privado `C04` |
| C05 | desejado | 1 | texto é inválido | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
