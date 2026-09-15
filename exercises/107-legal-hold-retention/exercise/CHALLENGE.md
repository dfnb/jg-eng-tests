# Desafio: Retenção com bloqueio legal

    ## Incidente ou solicitação

    A limpeza de documentos deve respeitar prazo, bloqueio legal e estado de exclusão já concluída.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **compliance**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - expirado é removido.
    - novo é mantido.
    - hold prevalece.
    - já removido é ignorado.
    - um dia antes mantém.

    O teste público demonstra o formato mínimo: a entrada `365|365|none|active` produz `delete`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
