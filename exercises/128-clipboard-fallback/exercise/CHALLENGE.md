# Desafio: Fallback de área de transferência

    ## Incidente ou solicitação

    A ação de copiar deve escolher API segura, fallback ou orientação manual conforme contexto e permissão.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **integração com navegador**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - API moderna em contexto seguro.
    - contexto inseguro usa fallback.
    - API ausente usa fallback.
    - permissão negada orienta manual.
    - prompt ainda tenta API.

    O teste público demonstra o formato mínimo: a entrada `yes|yes|granted` produz `clipboard-api`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
