# Avaliação: Invalidação por tags

    - **ID:** 55
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
    | C01 | mínimo | 3 | produto invalida detalhe/lista | teste privado `C01` |
| C02 | mínimo | 2 | usuário não invalida catálogo | teste privado `C02` |
| C03 | mínimo | 2 | tag ausente gera vazio | teste privado `C03` |
| C04 | intermediário | 2 | múltiplas tags localizam | teste privado `C04` |
| C05 | desejado | 1 | ordem de saída é estável | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
