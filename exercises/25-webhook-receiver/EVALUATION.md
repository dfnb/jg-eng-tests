# Avaliação: Recebimento de webhooks

    - **ID:** 25
    - **Tipo:** integration
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar integração autenticada, bytes brutos e idempotência.

    **Causa/omissão deliberada:** a assinatura é calculada sobre JSON normalizado e eventos repetidos são sempre aplicados.

    **Armadilha principal:** desserializar antes de verificar ou comparar segredos com igualdade comum.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | assinatura sobre corpo bruto é aceita | teste privado `C01` |
| C02 | mínimo | 3 | assinatura inválida é rejeitada | teste privado `C02` |
| C03 | mínimo | 2 | evento repetido não duplica efeito | teste privado `C03` |
| C04 | intermediário | 1 | JSON inválido assinado é rejeitado com segurança | teste privado `C04` |
| C05 | desejado | 1 | comparação usa tempo constante | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
