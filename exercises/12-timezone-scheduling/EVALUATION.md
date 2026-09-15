# Avaliação: Agendamento e fuso horário

    - **ID:** 12
    - **Tipo:** bugfix
    - **Nível:** beginner
    - **Duração:** 90 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar modelagem de tempo, conversão de fuso e testes determinísticos.

    **Causa/omissão deliberada:** a implementação usa `.Date` sobre o instante original e soma 24 horas em UTC.

    **Armadilha principal:** aplicar offset manual duas vezes ou usar `DateTime.Now`.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | data local usa o fuso informado | teste privado `C01` |
| C02 | mínimo | 2 | instante não é alterado | teste privado `C02` |
| C03 | mínimo | 2 | limites do dia são convertidos para UTC | teste privado `C03` |
| C04 | intermediário | 2 | dia de horário de verão pode ter duração diferente de 24h | teste privado `C04` |
| C05 | desejado | 1 | resultado independe do fuso da máquina | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
