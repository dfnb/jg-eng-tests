# Desafio: Resumo acessível de gráfico

    ## Incidente ou solicitação

    Um gráfico precisa produzir alternativa textual com tendência, mínimo e máximo a partir dos mesmos dados visuais.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **visualização acessível**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - tendência de alta.
    - tendência de baixa.
    - estável.
    - um ponto.
    - sem dados.

    O teste público demonstra o formato mínimo: a entrada `1,3,5` produz `up|min=1|max=5`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
