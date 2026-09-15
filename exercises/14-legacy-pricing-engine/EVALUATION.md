# Avaliação: Motor de preços legado

    - **ID:** 14
    - **Tipo:** refactoring
    - **Nível:** intermediate
    - **Duração:** 150 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar refatoração protegida, Strategy e Open/Closed sem overengineering.

    **Causa/omissão deliberada:** o motor ignora as estratégias recebidas e contém condicionais fixas.

    **Armadilha principal:** mudar a precedência ou aplicar todas as regras sobre o subtotal original.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | regras recebidas são executadas | teste privado `C01` |
| C02 | mínimo | 2 | ordem de aplicação é preservada | teste privado `C02` |
| C03 | mínimo | 2 | total nunca fica negativo | teste privado `C03` |
| C04 | intermediário | 2 | nova regra não requer mudança no motor | teste privado `C04` |
| C05 | desejado | 1 | lista vazia preserva subtotal | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
