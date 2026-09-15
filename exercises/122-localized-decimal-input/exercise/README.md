# Entrada decimal localizada

    Este repositório simula uma aplicação pequena em produção. Ele contém módulos de domínio, serviços, portas de integração, infraestrutura, estado e entrada pública. Nem todo arquivo participa diretamente do incidente: formar um mapa da base e seguir o fluxo é parte do trabalho.

    ## Produto

    Valores monetários digitados com separadores locais precisam virar representação canônica sem ambiguidades.

    ## Stack e organização

    React e TypeScript. O código de produção está em `src` e os testes públicos em `tests/`. As integrações externas são substituídas por contratos locais para manter a execução determinística.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    Preserve as APIs públicas e evite mudanças amplas antes de entender o caminho usado pela fachada.
