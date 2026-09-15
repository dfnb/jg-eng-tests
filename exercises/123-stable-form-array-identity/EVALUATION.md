# Avaliação: Identidade estável em formulários

    - **ID:** 123
    - **Área:** Frontend
    - **Tecnologias:** Angular e TypeScript
    - **Perfil:** pequena aplicação de produção
    - **Tempo sugerido:** 180 minutos

    ## Intenção pedagógica

    Avaliar navegação, delimitação de responsabilidade e implementação de formulários dinâmicos. O caminho da fachada até a política atravessa limites explícitos da aplicação; alterar arquivos não relacionados deve ser evitado.

    **Lacuna deliberada:** uma política interna contém uma implementação parcial plausível, enquanto infraestrutura, contratos, scripts e fluxos adjacentes estão prontos.

    **Armadilha:** criar uma segunda implementação fora do fluxo real, alterar a fachada para contornar a arquitetura ou confundir módulos plausíveis com arquivos que precisam ser modificados.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Teste |
    | --- | --- | ---: | --- | --- |
    | C01 | minimum | 3 | remove por ID | `C01` |
| C02 | minimum | 2 | adiciona ao fim | `C02` |
| C03 | minimum | 2 | adiciona na posição | `C03` |
| C04 | intermediate | 2 | ID duplicado não entra | `C04` |
| C05 | desired | 1 | remoção ausente não muda | `C05` |

    O grader entra pela API pública. Soluções internas diferentes da referência são aceitas desde que preservem o contrato e todos os resultados observáveis.
