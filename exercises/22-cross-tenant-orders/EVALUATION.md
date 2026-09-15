# Avaliação: Pedidos de outro cliente

    - **ID:** 22
    - **Tipo:** security
    - **Nível:** intermediate
    - **Duração:** 90 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar Broken Object Level Authorization e centralização de política.

    **Causa/omissão deliberada:** somente a existência do pedido é verificada.

    **Armadilha principal:** confiar em customerId do request ou proteger apenas leitura.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | leitura cruzada é negada | teste privado `C01` |
| C02 | mínimo | 3 | alteração e cancelamento cruzados são negados | teste privado `C02` |
| C03 | mínimo | 2 | proprietário mantém acesso | teste privado `C03` |
| C04 | intermediário | 1 | recurso alheio não revela existência | teste privado `C04` |
| C05 | desejado | 1 | política é aplicada aos três métodos | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
