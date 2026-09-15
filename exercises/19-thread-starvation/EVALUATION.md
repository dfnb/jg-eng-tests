# Avaliação: API com starvation

    - **ID:** 19
    - **Tipo:** async
    - **Nível:** advanced
    - **Duração:** 150 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar async/await, concorrência limitada e propagação de cancelamento.

    **Causa/omissão deliberada:** uso de `.Result` em loop sequencial.

    **Armadilha principal:** envolver I/O em `Task.Run` ou lançar todas as tarefas sem limite.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | caminho não bloqueia Task sincronamente | teste privado `C01` |
| C02 | mínimo | 2 | resultados preservam a ordem | teste privado `C02` |
| C03 | mínimo | 2 | concorrência respeita o limite | teste privado `C03` |
| C04 | intermediário | 2 | cancelamento chega ao provedor | teste privado `C04` |
| C05 | desejado | 1 | lista vazia retorna imediatamente | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
