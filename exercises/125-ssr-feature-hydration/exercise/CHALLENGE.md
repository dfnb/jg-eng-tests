# Desafio: Paridade de feature flags no SSR

    ## Incidente ou solicitação

    Servidor e cliente precisam usar o mesmo snapshot de flags durante a hidratação para evitar reconstrução da árvore.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **renderização híbrida**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - snapshots iguais hidratam.
    - ordem não importa.
    - flag extra reconstrói.
    - flag ausente reconstrói.
    - dois vazios hidratam.

    O teste público demonstra o formato mínimo: a entrada `a,b|a,b` produz `hydrate`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
