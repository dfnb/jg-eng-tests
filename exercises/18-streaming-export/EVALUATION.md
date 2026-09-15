# Avaliação: Exportação sem memória

    - **ID:** 18
    - **Tipo:** performance
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar streaming, backpressure, escaping e cancelamento.

    **Causa/omissão deliberada:** a implementação materializa toda a fonte antes de começar a produzir.

    **Armadilha principal:** paginar a leitura e ainda acumular todas as strings.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | todas as linhas são emitidas na ordem | teste privado `C01` |
| C02 | mínimo | 3 | primeira linha não exige leitura integral | teste privado `C02` |
| C03 | mínimo | 2 | campos CSV recebem escaping | teste privado `C03` |
| C04 | intermediário | 1 | cancelamento interrompe enumeração | teste privado `C04` |
| C05 | desejado | 1 | fonte vazia é suportada | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
