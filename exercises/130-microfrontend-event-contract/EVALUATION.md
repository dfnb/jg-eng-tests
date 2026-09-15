# Avaliação: Contrato de eventos entre microfrontends

    - **ID:** 130
    - **Área:** Frontend
    - **Tecnologias:** React e TypeScript
    - **Perfil:** pequena aplicação de produção
    - **Tempo sugerido:** 180 minutos

    ## Intenção pedagógica

    Avaliar navegação, delimitação de responsabilidade e implementação de arquitetura frontend. O caminho da fachada até a política atravessa limites explícitos da aplicação; alterar arquivos não relacionados deve ser evitado.

    **Lacuna deliberada:** uma política interna contém uma implementação parcial plausível, enquanto infraestrutura, contratos, scripts e fluxos adjacentes estão prontos.

    **Armadilha:** criar uma segunda implementação fora do fluxo real, alterar a fachada para contornar a arquitetura ou confundir módulos plausíveis com arquivos que precisam ser modificados.

    ## Critérios automatizados

    | ID | Nível | Peso | Condição binária | Teste |
    | --- | --- | ---: | --- | --- |
    | C01 | minimum | 3 | evento válido entra | `C01` |
| C02 | minimum | 2 | namespace externo ignora | `C02` |
| C03 | minimum | 2 | versão antiga rejeita | `C03` |
| C04 | intermediate | 2 | ID obrigatório | `C04` |
| C05 | desired | 1 | timestamp obrigatório | `C05` |

    O grader entra pela API pública. Soluções internas diferentes da referência são aceitas desde que preservem o contrato e todos os resultados observáveis.
