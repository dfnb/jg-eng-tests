# Avaliação: Checkout modular

    - **ID:** 06
    - **Tipo:** refactoring
    - **Nível:** intermediate
    - **Duração:** 150 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar limites arquiteturais, injeção e comportamento transacional sem exigir uma estrutura interna única.

    **Causa/omissão deliberada:** a implementação confirma antes do pagamento e não compensa estoque.

    **Armadilha principal:** corrigir a ordem feliz e esquecer a falha depois da reserva.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | pedido válido é reservado, cobrado e confirmado | teste privado `C01` |
| C02 | mínimo | 3 | falha de pagamento não confirma | teste privado `C02` |
| C03 | mínimo | 2 | falha de pagamento libera estoque | teste privado `C03` |
| C04 | intermediário | 1 | carrinho vazio não chama gateways | teste privado `C04` |
| C05 | desejado | 1 | dependências são substituíveis por interfaces | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
