# Avaliação: Importação de catálogo

    - **ID:** 04
    - **Tipo:** data
    - **Nível:** beginner
    - **Duração:** 90 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar parsing, validação e atomicidade de manipulação de dados.

    **Causa/omissão deliberada:** o parser usa `Split(',')`, ignora duplicidade e retorna linhas válidas mesmo com erro.

    **Armadilha principal:** tratar apenas o fixture simples e quebrar vírgulas dentro de aspas.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | CSV válido é convertido | teste privado `C01` |
| C02 | mínimo | 2 | campos com vírgula e aspas são lidos | teste privado `C02` |
| C03 | mínimo | 2 | SKU duplicado aponta a linha | teste privado `C03` |
| C04 | intermediário | 2 | erro torna o lote atômico | teste privado `C04` |
| C05 | desejado | 1 | preço usa cultura invariável | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
