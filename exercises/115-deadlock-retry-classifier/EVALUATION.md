# Avaliação: Classificação de retry de banco

    - **ID:** 115
    - **Área:** Backend
    - **Tecnologias:** C# e .NET 10
    - **Perfil:** pequena aplicação de produção
    - **Tempo sugerido:** 180 minutos

    ## Intenção pedagógica

    Avaliar navegação, delimitação de responsabilidade e implementação de persistência resiliente. O caminho da fachada até a política atravessa limites explícitos da aplicação; alterar arquivos não relacionados deve ser evitado.

    **Lacuna deliberada:** uma política interna contém uma implementação parcial plausível, enquanto infraestrutura, contratos, scripts e fluxos adjacentes estão prontos.

    **Armadilha:** criar uma segunda implementação fora do fluxo real, alterar a fachada para contornar a arquitetura ou confundir módulos plausíveis com arquivos que precisam ser modificados.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Teste |
    | --- | --- | ---: | --- | --- |
    | C01 | minimum | 3 | deadlock repete | `C01` |
| C02 | minimum | 2 | última tentativa esgota | `C02` |
| C03 | minimum | 2 | unique não repete | `C03` |
| C04 | intermediate | 2 | timeout não é assumido | `C04` |
| C05 | desired | 1 | zero tentativas ainda repete | `C05` |

    O grader entra pela API pública. Soluções internas diferentes da referência são aceitas desde que preservem o contrato e todos os resultados observáveis.
