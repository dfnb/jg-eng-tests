# Desafio: Precedência de configuração regional

    ## Incidente ou solicitação

    A aplicação combina configuração global, regional e de tenant sem deixar valor vazio sobrescrever uma configuração válida.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **configuração**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - tenant vence.
    - regional cobre tenant vazio.
    - global é fallback.
    - espaço não sobrescreve.
    - tudo ausente é unset.

    O teste público demonstra o formato mínimo: a entrada `global|regional|tenant` produz `tenant`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
