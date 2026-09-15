# Avaliação: Totais monetários

    - **ID:** 13
    - **Tipo:** bugfix
    - **Nível:** beginner
    - **Duração:** 75 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Avaliar precisão monetária e tradução exata de regra contábil.

    **Causa/omissão deliberada:** a implementação converte para `double` e arredonda apenas o total final.

    **Armadilha principal:** apenas trocar o tipo sem corrigir a ordem de arredondamento.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | cada linha é arredondada antes da soma | teste privado `C01` |
| C02 | mínimo | 2 | cálculo não perde precisão decimal | teste privado `C02` |
| C03 | mínimo | 2 | imposto usa a soma líquida | teste privado `C03` |
| C04 | intermediário | 2 | estorno é simétrico | teste privado `C04` |
| C05 | desejado | 1 | meio centavo usa AwayFromZero | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
