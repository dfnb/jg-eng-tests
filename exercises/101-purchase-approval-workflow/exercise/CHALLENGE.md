# Desafio: Fluxo de aprovação de compras

    ## Incidente ou solicitação

    Uma plataforma de compras precisa decidir a próxima etapa usando valor, centro de custo e segregação de funções.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **workflow de domínio**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - compra pequena é aprovada.
    - valor médio exige gerente.
    - alto valor exige diretor.
    - sem orçamento rejeita.
    - autor não aprova a própria compra.

    O teste público demonstra o formato mínimo: a entrada `500|ana|bia|yes` produz `approved`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
