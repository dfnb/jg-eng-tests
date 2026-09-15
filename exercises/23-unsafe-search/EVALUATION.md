# Avaliação: Busca vulnerável

    - **ID:** 23
    - **Tipo:** security
    - **Nível:** beginner
    - **Duração:** 75 minutos
    - **Tecnologias:** dotnet10, sql

    ## Intenção e estado inicial

    Avaliar SQL injection em valores e identificadores.

    **Causa/omissão deliberada:** todas as entradas são interpoladas diretamente.

    **Armadilha principal:** parametrizar o filtro e ainda interpolar sort arbitrário.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | filtro usa parâmetro | teste privado `C01` |
| C02 | mínimo | 3 | coluna possui allowlist | teste privado `C02` |
| C03 | mínimo | 2 | direção possui allowlist | teste privado `C03` |
| C04 | intermediário | 1 | entrada inválida não inclui detalhe SQL | teste privado `C04` |
| C05 | desejado | 1 | busca legítima preserva contrato | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
