# Desafio: Preferência por movimento reduzido

    ## Incidente ou solicitação

    Transições precisam respeitar prefers-reduced-motion mantendo feedback sem animação contínua.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **acessibilidade visual**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - reduce remove transição.
    - reduce mantém progresso estático.
    - normal anima modal.
    - normal anima progresso.
    - efeito desconhecido respeita reduce.

    O teste público demonstra o formato mínimo: a entrada `reduce|modal` produz `instant`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
