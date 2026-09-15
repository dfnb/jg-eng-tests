# Avaliação: Tokenização de busca

    - **ID:** 50
    - **Área:** backend
    - **Foco:** queries
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de queries em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | termos viram tokens | teste privado `C01` |
| C02 | mínimo | 2 | espaços repetidos somem | teste privado `C02` |
| C03 | mínimo | 2 | percentual é escapado | teste privado `C03` |
| C04 | intermediário | 2 | underscore é escapado | teste privado `C04` |
| C05 | desejado | 1 | barra é escapada primeiro | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
