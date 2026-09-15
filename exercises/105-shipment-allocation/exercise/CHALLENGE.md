# Desafio: Alocação de remessas

    ## Incidente ou solicitação

    Pedidos devem ser alocados ao depósito com estoque suficiente e menor distância, usando ID como desempate estável.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **algoritmos de domínio**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - menor distância vence.
    - estoque insuficiente é ignorado.
    - ID desempata.
    - nenhum candidato.
    - lista vazia.

    O teste público demonstra o formato mínimo: a entrada `2|a:5:20,b:5:10` produz `b`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
