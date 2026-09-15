# Avaliação: Cupons concorrentes

    - **ID:** 20
    - **Tipo:** concurrency
    - **Nível:** advanced
    - **Duração:** 150 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar race condition, atomicidade e diferença entre lock local e recurso compartilhado.

    **Causa/omissão deliberada:** check-then-act sem sincronização.

    **Armadilha principal:** proteger apenas um contador da instância do serviço.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | primeiro resgate vence | teste privado `C01` |
| C02 | mínimo | 3 | somente um resgate concorrente vence | teste privado `C02` |
| C03 | mínimo | 2 | auditoria contém um evento | teste privado `C03` |
| C04 | intermediário | 1 | duas instâncias mantêm a garantia | teste privado `C04` |
| C05 | desejado | 1 | cupom inexistente não altera estado | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
