# Desafio: Restauração de wizard

    ## Incidente ou solicitação

    Um fluxo multietapa deve restaurar somente etapas válidas e nunca pular uma etapa obrigatória incompleta.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **formulários multietapa**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - restaura etapa válida.
    - não pula primeira inválida.
    - limita na inválida.
    - todas válidas permitem fim.
    - índice negativo vira zero.

    O teste público demonstra o formato mínimo: a entrada `1|yes,no,no` produz `1`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
