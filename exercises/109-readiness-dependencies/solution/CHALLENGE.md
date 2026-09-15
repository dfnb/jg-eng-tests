# Desafio: Readiness de dependências

    ## Incidente ou solicitação

    O endpoint de readiness deve distinguir dependências obrigatórias das opcionais e não confundir liveness com prontidão.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **observabilidade**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - todas obrigatórias disponíveis.
    - banco indisponível bloqueia.
    - opcional não bloqueia.
    - sem dependências obrigatórias.
    - lista vazia.

    O teste público demonstra o formato mínimo: a entrada `required:db:up,required:queue:up` produz `ready`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
