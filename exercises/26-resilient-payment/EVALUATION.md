# Avaliação: Pagamento resiliente

    - **ID:** 26
    - **Tipo:** integration
    - **Nível:** advanced
    - **Duração:** 150 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar retry seguro, idempotência, cancelamento e circuit breaker.

    **Causa/omissão deliberada:** toda falha é repetida com uma nova chave e não existe breaker.

    **Armadilha principal:** repetir POST com GUID novo ou retry de erro permanente.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | somente transientes são repetidas | teste privado `C01` |
| C02 | mínimo | 3 | tentativas preservam chave idempotente | teste privado `C02` |
| C03 | mínimo | 2 | máximo de três tentativas | teste privado `C03` |
| C04 | intermediário | 1 | cancelamento interrompe tentativas | teste privado `C04` |
| C05 | desejado | 1 | breaker evita chamadas após limiar | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
