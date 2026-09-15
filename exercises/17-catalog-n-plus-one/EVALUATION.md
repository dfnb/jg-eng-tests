# Avaliação: Catálogo N+1

    - **ID:** 17
    - **Tipo:** performance
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar diagnóstico de I/O repetitivo e correção mensurável de query.

    **Causa/omissão deliberada:** há uma consulta de estoque por produto.

    **Armadilha principal:** trocar N+1 por estado global ou remover campos da resposta.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | valores retornados estão corretos | teste privado `C01` |
| C02 | mínimo | 3 | no máximo duas consultas são executadas | teste privado `C02` |
| C03 | mínimo | 2 | paginação limita os produtos | teste privado `C03` |
| C04 | intermediário | 1 | produto sem estoque retorna zero | teste privado `C04` |
| C05 | desejado | 1 | chamada seguinte observa atualização do repositório | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
