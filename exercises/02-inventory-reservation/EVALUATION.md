# Avaliação: Reserva de estoque

    - **ID:** 02
    - **Tipo:** bugfix
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar diagnóstico de transição de estado, idempotência e atomicidade.

    **Causa/omissão deliberada:** o cancelamento não devolve a quantidade e não protege a operação composta.

    **Armadilha principal:** incrementar em todo cancelamento e permitir devolução dupla.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | primeiro cancelamento devolve saldo | teste privado `C01` |
| C02 | mínimo | 3 | cancelamento repetido não duplica saldo | teste privado `C02` |
| C03 | mínimo | 2 | reserva ativa reduz saldo | teste privado `C03` |
| C04 | intermediário | 1 | estoque insuficiente não cria reserva | teste privado `C04` |
| C05 | desejado | 1 | cancelamentos concorrentes devolvem uma vez | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
