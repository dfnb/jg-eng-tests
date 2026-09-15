# Desafio: Descontinuação de API

    ## Incidente ou solicitação

    Versões depreciadas devem emitir Deprecation e Sunset coerentes sem marcar versões ainda suportadas.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **governança de API**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - versão antiga deprecia.
    - versão atual suporta.
    - versão futura suporta.
    - sunset é preservado.
    - primeira versão atual.

    O teste público demonstra o formato mínimo: a entrada `1|2|2030-01-01` produz `deprecated|sunset=2030-01-01`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
