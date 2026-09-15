# Desafio: Reconstrução de histórico de auditoria

    ## Incidente ou solicitação

    Consultas históricas precisam reconstruir o valor vigente em um instante, mesmo quando eventos chegam fora de ordem.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **dados temporais**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - usa último evento anterior.
    - ordena eventos recebidos fora de ordem.
    - antes da criação é ausente.
    - evento na borda vale.
    - sem eventos é ausente.

    O teste público demonstra o formato mínimo: a entrada `20|10:draft,20:open,30:closed` produz `open`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
