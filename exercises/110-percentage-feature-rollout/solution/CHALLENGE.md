# Desafio: Rollout percentual de feature

    ## Incidente ou solicitação

    Uma feature deve ser atribuída de forma determinística por usuário, respeitando percentuais zero e cem.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **entrega progressiva**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - zero desliga.
    - cem liga.
    - bucket abaixo liga.
    - bucket na borda desliga.
    - mesmo usuário é estável.

    O teste público demonstra o formato mínimo: a entrada `ana|0` produz `off`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
