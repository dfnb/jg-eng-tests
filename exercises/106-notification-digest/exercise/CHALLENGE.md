# Desafio: Agrupamento de notificações

    ## Incidente ou solicitação

    Um job de digest agrupa notificações por destinatário e canal, remove duplicatas e preserva ordem determinística.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **processamento em lote**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - agrupa em ordem estável.
    - remove duplicata.
    - canais ficam separados.
    - destinatários ficam separados.
    - vazio produz vazio.

    O teste público demonstra o formato mínimo: a entrada `b:email:2,a:sms:1` produz `a:sms:1,b:email:2`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
