# Desafio: Encerramento gracioso de workers

    ## Incidente ou solicitação

    Ao receber shutdown, o worker para de aceitar itens e aguarda somente o trabalho em andamento até o prazo.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **lifecycle**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - trabalho ativo drena.
    - prazo encerra à força.
    - fila não é iniciada.
    - sem trabalho para.
    - ativo ignora fila nova.

    O teste público demonstra o formato mínimo: a entrada `2|5|30` produz `drain:2`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
