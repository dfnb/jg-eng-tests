# Desafio: Ordenação de chunks em streaming

    ## Incidente ou solicitação

    Chunks de uma resposta podem chegar fora de ordem e só devem liberar o prefixo contínuo já disponível.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **renderização incremental**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - primeiro chunk libera.
    - gap aguarda.
    - fora de ordem completa prefixo.
    - continua de checkpoint.
    - vazio aguarda.

    O teste público demonstra o formato mínimo: a entrada `0|0:A` produz `1|A`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
