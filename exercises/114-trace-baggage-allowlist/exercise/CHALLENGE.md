# Desafio: Privacidade em baggage de tracing

    ## Incidente ou solicitação

    Propagação de tracing deve manter somente chaves permitidas, limitar tamanho e ordenar a saída.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **telemetria**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - mantém allowlist.
    - remove segredo.
    - remove valor longo.
    - ordena chaves.
    - vazio.

    O teste público demonstra o formato mínimo: a entrada `tenant=t1,region=br` produz `region=br,tenant=t1`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
