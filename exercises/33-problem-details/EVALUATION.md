# Avaliação: Erros com Problem Details

    - **ID:** 33
    - **Área:** backend
    - **Foco:** contratos de erro
    - **Tecnologias:** C#, .NET 10

    ## Intenção

    Avaliar se o estudante transforma uma regra de contratos de erro em comportamento previsível, incluindo limites que aparecem em produção sem codificar somente o caminho feliz.

    **Omissão deliberada:** a política inicial preserva a assinatura, mas ainda não implementa o domínio.

    **Armadilha:** assumir que o exemplo público descreve todas as entradas ou alterar a API em vez de completar seu comportamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | 404 possui tipo estável | teste privado `C01` |
| C02 | mínimo | 2 | 409 representa conflito | teste privado `C02` |
| C03 | mínimo | 2 | 422 usa validation | teste privado `C03` |
| C04 | intermediário | 2 | trace é preservado | teste privado `C04` |
| C05 | desejado | 1 | mensagem interna não é incluída | teste privado `C05` |

    Uma solução alternativa é válida quando preserva o contrato e passa os casos observáveis. A referência não impõe uma organização interna específica.
