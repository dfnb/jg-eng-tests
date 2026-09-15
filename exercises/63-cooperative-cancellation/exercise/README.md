# Cancelamento cooperativo

    Este repositório simula um componente de uma aplicação empresarial. A regra isolada representa uma decisão encontrada em produção e usa texto como formato de fixture para manter o exercício autocontido.

    ## Stack e arquitetura

    C# com .NET 10. A API pública está em `src/Challenge/Challenge.cs`; os testes públicos verificam apenas o contrato básico.

    ## Executar

    ```bash
    ./scripts/setup.sh
    ./scripts/test.sh
    ./scripts/lint.sh
    ```

    Não são necessárias credenciais, banco de dados ou conexão de rede.
