# Desafio: Jitter de cache

    ## Contexto

    Adicionar jitter determinístico por chave para evitar expiração simultânea.

    ## Pedido

    Complete `Policy.Evaluate` de acordo com o contrato descrito pelo domínio e preserve a assinatura pública. Investigue os casos de borda coerentes com **cache** e acrescente testes de regressão quando necessário.

    ## Restrições

    A solução deve ser determinística, funcionar para entradas equivalentes além dos exemplos públicos e permanecer compatível com .NET 10. Não adicione dependências ou serviços externos.

    ## Verificação

    Execute `./scripts/test.sh` e `./scripts/lint.sh`. Os testes de avaliação cobrem situações adicionais que não são reveladas no repositório do estudante.
