# Avaliação: Serviço de encurtamento

    - **ID:** 27
    - **Tipo:** greenfield
    - **Nível:** intermediate
    - **Duração:** 240 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar criação de componente do zero, contrato, validação e concorrência sem prescrever arquitetura.

    **Causa/omissão deliberada:** métodos lançam `NotImplementedException`.

    **Armadilha principal:** validar URL apenas por prefixo ou sobrescrever colisão.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | criar e resolver preserva URL | teste privado `C01` |
| C02 | mínimo | 2 | somente HTTP/HTTPS absoluto é aceito | teste privado `C02` |
| C03 | mínimo | 2 | colisão não sobrescreve link | teste privado `C03` |
| C04 | intermediário | 2 | duas instâncias geram códigos únicos | teste privado `C04` |
| C05 | desejado | 1 | código ausente retorna null | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
