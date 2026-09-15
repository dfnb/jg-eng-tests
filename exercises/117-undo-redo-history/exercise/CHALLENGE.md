# Desafio: Histórico de undo e redo

    ## Incidente ou solicitação

    Um editor precisa calcular corretamente o estado após comandos, undo, redo e nova edição que invalida o futuro.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **estado reversível**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - undo restaura.
    - redo reaplica.
    - nova edição limpa redo.
    - undo vazio é seguro.
    - vários undos.

    O teste público demonstra o formato mínimo: a entrada `set:a,set:b,undo` produz `a`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
