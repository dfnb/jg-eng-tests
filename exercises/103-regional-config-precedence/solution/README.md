# Precedência de configuração regional

    Este repositório simula uma aplicação pequena em produção. Ele contém módulos de domínio, serviços, portas de integração, infraestrutura, estado e entrada pública. Nem todo arquivo participa diretamente do incidente: formar um mapa da base e seguir o fluxo é parte do trabalho.

    ## Produto

    A aplicação combina configuração global, regional e de tenant sem deixar valor vazio sobrescrever uma configuração válida.

    ## Stack e organização

    C# e .NET 10. O código de produção está em `src/ProductionApp` e os testes públicos em `tests/`. As integrações externas são substituídas por contratos locais para manter a execução determinística.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    Preserve as APIs públicas e evite mudanças amplas antes de entender o caminho usado pela fachada.
