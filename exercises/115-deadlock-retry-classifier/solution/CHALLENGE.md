# Desafio: Classificação de retry de banco

    ## Incidente ou solicitação

    A camada de dados deve repetir somente deadlocks transitórios e nunca violações permanentes ou tentativas já esgotadas.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **persistência resiliente**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - deadlock repete.
    - última tentativa esgota.
    - unique não repete.
    - timeout não é assumido.
    - zero tentativas ainda repete.

    O teste público demonstra o formato mínimo: a entrada `deadlock|1|3` produz `retry`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
