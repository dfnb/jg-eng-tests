# Desafio: Estorno no razão contábil

    ## Incidente ou solicitação

    Um estorno deve produzir lançamentos de sinal oposto, na moeda original, sem alterar o lançamento histórico.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **invariantes contábeis**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - débito vira crédito.
    - crédito vira débito.
    - centavos são preservados.
    - valor não muda de sinal.
    - moeda é normalizada.

    O teste público demonstra o formato mínimo: a entrada `25.5|debit|brl` produz `credit|25.50|BRL`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
