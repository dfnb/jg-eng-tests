# Avaliação: Desconto de fidelidade

    - **ID:** 01
    - **Tipo:** feature
    - **Nível:** beginner
    - **Duração:** 90 minutos
    - **Tecnologias:** dotnet10

    ## Intenção e estado inicial

    Distinguir implementação de feature orientada por regra, cuidado com dinheiro e preservação de comportamento.

    **Causa/omissão deliberada:** o método ignora o nível de fidelidade.

    **Armadilha principal:** aplicar desconto depois do imposto ou arredondar cedo demais.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Verificação |
    | --- | --- | ---: | --- | --- |
    | C01 | mínimo | 3 | Gold recebe 10% | teste privado `C01` |
| C02 | mínimo | 3 | Silver recebe 5% | teste privado `C02` |
| C03 | mínimo | 2 | desconto precede imposto | teste privado `C03` |
| C04 | intermediário | 1 | nível desconhecido não desconta | teste privado `C04` |
| C05 | desejado | 1 | arredondamento de meio centavo segue a política | teste privado `C05` |

    ## Soluções aceitas

    Qualquer implementação que preserve o contrato e passe pelos casos comportamentais é aceita. Os testes não exigem os mesmos nomes ou a mesma organização interna da referência, exceto pelas APIs iniciais protegidas.

    ## Validação

    O estado inicial deve compilar e passar nos testes públicos. A solução de referência deve passar no grader privado. Implementações que tratem apenas o exemplo público devem falhar em pelo menos um critério.
