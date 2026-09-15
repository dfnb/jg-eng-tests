# Desafio: Contrato de eventos entre microfrontends

    ## Incidente ou solicitação

    Eventos entre aplicações precisam validar versão, namespace e campos obrigatórios antes de atravessar a fronteira.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **arquitetura frontend**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - evento válido entra.
    - namespace externo ignora.
    - versão antiga rejeita.
    - ID obrigatório.
    - timestamp obrigatório.

    O teste público demonstra o formato mínimo: a entrada `commerce.order|v2|id,timestamp,total` produz `accept`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
