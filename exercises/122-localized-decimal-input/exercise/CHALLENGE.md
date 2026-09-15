# Desafio: Entrada decimal localizada

    ## Incidente ou solicitação

    Valores monetários digitados com separadores locais precisam virar representação canônica sem ambiguidades.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **internacionalização**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - pt-BR converte vírgula.
    - en-US converte agrupamento.
    - inteiro recebe centavos.
    - texto inválido.
    - espaços são aceitos.

    O teste público demonstra o formato mínimo: a entrada `pt-BR|1.234,56` produz `1234.56`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
