# Desafio: Identidade estável em formulários

    ## Incidente ou solicitação

    Linhas adicionadas e removidas devem preservar IDs estáveis para não trocar foco nem estado de validação.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **formulários dinâmicos**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - remove por ID.
    - adiciona ao fim.
    - adiciona na posição.
    - ID duplicado não entra.
    - remoção ausente não muda.

    O teste público demonstra o formato mínimo: a entrada `a,b,c|remove:b` produz `a,c`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
