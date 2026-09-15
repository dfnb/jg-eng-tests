# Desafio: Autosave versionado

    ## Incidente ou solicitação

    O autosave deve ignorar respostas antigas e distinguir conflito de versão de falha de rede.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **persistência de rascunho**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - resposta atual aplica.
    - resposta antiga ignora.
    - resposta futura ignora.
    - conflito abre resolução.
    - rede agenda retry.

    O teste público demonstra o formato mínimo: a entrada `3|3|ok` produz `apply`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
