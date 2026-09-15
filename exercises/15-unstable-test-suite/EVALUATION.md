# Avaliação: Suíte de testes instável

    - **ID:** 15
    - **Tipo:** quality
    - **Nível:** intermediate
    - **Duração:** 90 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar diagnóstico de flakiness e design para testabilidade.

    **Causa/omissão deliberada:** o serviço usa relógio real e `Random.Shared`, ignorando dependências.

    **Armadilha principal:** desligar paralelismo, adicionar retry ou espera.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | expiração usa o relógio injetado | teste privado `C01` |
| C02 | mínimo | 2 | nonce usa a fonte injetada | teste privado `C02` |
| C03 | mínimo | 2 | mesmas dependências geram resultado reproduzível | teste privado `C03` |
| C04 | intermediário | 2 | instâncias não compartilham estado | teste privado `C04` |
| C05 | desejado | 1 | código não usa relógio ou Random globais | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
