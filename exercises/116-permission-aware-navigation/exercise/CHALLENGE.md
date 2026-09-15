# Desafio: Navegação orientada por permissões

    ## Incidente ou solicitação

    O menu deve ocultar ações indisponíveis sem usar isso como substituto da autorização do servidor.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **autorização de interface**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - mostra rota permitida.
    - oculta rota negada.
    - múltiplas permissões.
    - rota pública permanece.
    - lista vazia.

    O teste público demonstra o formato mínimo: a entrada `orders:read|home=,orders=orders:read` produz `home,orders`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
