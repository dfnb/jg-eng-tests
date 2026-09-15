# Avaliação: Consumidor idempotente

    - **ID:** 21
    - **Tipo:** distributed-concurrency
    - **Nível:** advanced
    - **Duração:** 180 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar idempotência distribuída e fronteira transacional.

    **Causa/omissão deliberada:** cada consumidor mantém seu próprio HashSet e grava o efeito antes de marcar a mensagem.

    **Armadilha principal:** deduplicar apenas em memória por instância ou marcar antes do efeito.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | redelivery cria uma fatura | teste privado `C01` |
| C02 | mínimo | 3 | duas instâncias compartilham deduplicação | teste privado `C02` |
| C03 | mínimo | 2 | falha permite retry sem duplicação | teste privado `C03` |
| C04 | intermediário | 1 | chaves distintas geram efeitos distintos | teste privado `C04` |
| C05 | desejado | 1 | mensagem já concluída retorna sucesso idempotente | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
