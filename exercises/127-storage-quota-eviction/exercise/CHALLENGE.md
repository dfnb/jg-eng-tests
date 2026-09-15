# Desafio: Evicção por quota do navegador

    ## Incidente ou solicitação

    O cache local deve remover entradas menos recentes até caber, preservando itens fixados.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **armazenamento local**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - cabe sem remover.
    - remove mais antigo.
    - remove até caber.
    - fixado é preservado.
    - vazio recebe item.

    O teste público demonstra o formato mínimo: a entrada `100|10|a:20:5:no` produz `none`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
