# Desafio: Imports tree-shakable

    ## Contexto

    Classificar import granular como seguro e barrel amplo como custo evitável.

    ## Pedido

    Complete `evaluate` preservando sua exportação e integre a decisão ao componente quando isso for relevante. Considere os limites naturais de **bundle size**, não somente o caminho mais comum.

    ## Restrições

    Mantenha TypeScript, Angular e o formato textual do contrato. Não adicione chamadas de rede, dependências ou respostas codificadas para fixtures específicas.

    ## Verificação

    Execute `./scripts/test.sh` e `./scripts/lint.sh`. A avaliação privada contém entradas adicionais, inclusive casos de borda.
