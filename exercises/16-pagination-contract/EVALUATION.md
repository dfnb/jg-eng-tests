# Avaliação: Contrato de paginação

    - **ID:** 16
    - **Tipo:** regression
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar correção de regressão em contrato de paginação e ordenação estável.

    **Causa/omissão deliberada:** o filtro do cursor considera apenas a data.

    **Armadilha principal:** deduplicar no cliente ou usar índice da lista como cursor.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | itens aparecem uma única vez entre páginas | teste privado `C01` |
| C02 | mínimo | 2 | empates usam ID ascendente | teste privado `C02` |
| C03 | mínimo | 2 | cursor é exclusivo | teste privado `C03` |
| C04 | intermediário | 2 | entrada desordenada gera saída estável | teste privado `C04` |
| C05 | desejado | 1 | take inválido é rejeitado | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
