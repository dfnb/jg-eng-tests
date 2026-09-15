# Avaliação: Upload de documentos

    - **ID:** 24
    - **Tipo:** security
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar segurança de upload e uso seguro de filesystem.

    **Causa/omissão deliberada:** o nome e MIME declarados são confiados e o stream inteiro é copiado sem limite.

    **Armadilha principal:** validar somente extensão ou `Content-Type`.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | traversal não escapa do root | teste privado `C01` |
| C02 | mínimo | 3 | limite é aplicado durante leitura | teste privado `C02` |
| C03 | mínimo | 2 | conteúdo incompatível é rejeitado | teste privado `C03` |
| C04 | intermediário | 1 | nomes armazenados não colidem | teste privado `C04` |
| C05 | desejado | 1 | rejeição não deixa arquivo parcial | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
