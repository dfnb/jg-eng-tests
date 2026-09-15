# Avaliação: Relatório de vendas

    - **ID:** 03
    - **Tipo:** data
    - **Nível:** intermediate
    - **Duração:** 120 minutos
    - **Tecnologias:** dotnet10, linq

    ## Intenção e estado inicial

    Avaliar semântica de agregação, limites temporais e ordem correta das operações de query.

    **Causa/omissão deliberada:** a implementação pagina eventos antes da agregação e inclui estados inválidos.

    **Armadilha principal:** agregar depois de `Skip/Take` ou usar limite final inclusivo.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | canceladas são excluídas | teste privado `C01` |
| C02 | mínimo | 2 | intervalo é semiaberto | teste privado `C02` |
| C03 | mínimo | 2 | agregação precede paginação | teste privado `C03` |
| C04 | intermediário | 2 | ordenação possui desempate estável | teste privado `C04` |
| C05 | desejado | 1 | paginação inválida é rejeitada | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
