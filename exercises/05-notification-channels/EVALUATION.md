# Avaliação: Canais de notificação

    - **ID:** 05
    - **Tipo:** design-patterns
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar Strategy/DI, composição e isolamento de falhas.

    **Causa/omissão deliberada:** o orquestrador reconhece apenas e-mail e interrompe na primeira exceção.

    **Armadilha principal:** adicionar outro `if` por canal ou capturar erro ao redor do lote inteiro.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | todos os canais preferidos registrados são chamados | teste privado `C01` |
| C02 | mínimo | 2 | canal desconhecido é ignorado | teste privado `C02` |
| C03 | mínimo | 2 | falha é isolada por canal | teste privado `C03` |
| C04 | intermediário | 2 | novo canal funciona sem alteração do orquestrador | teste privado `C04` |
| C05 | desejado | 1 | resultado informa sucesso e falha por canal | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
