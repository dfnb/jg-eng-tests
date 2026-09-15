# Desafio: Cache normalizado de entidades

    ## Incidente ou solicitação

    Atualizações parciais devem mesclar entidades por ID sem duplicar referências nas listas.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **gerenciamento de estado**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - atualiza entidade.
    - insere entidade.
    - ordena por ID.
    - vazio aceita primeira.
    - valor vazio é mantido.

    O teste público demonstra o formato mínimo: a entrada `a:old,b:same|a:new` produz `a:new,b:same`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
