# Desafio: Paginação para impressão

    ## Incidente ou solicitação

    Relatórios impressos devem calcular quebras sem separar cabeçalho e primeira linha de uma seção.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **mídia impressa**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - uma página.
    - quebra antes da seção.
    - múltiplas páginas.
    - seção do tamanho da página.
    - seção maior sinaliza.

    O teste público demonstra o formato mínimo: a entrada `100|20,30,40` produz `1`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
