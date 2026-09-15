# Desafio: Rotação de segredo sem indisponibilidade

    ## Incidente ou solicitação

    Durante uma rotação, assinaturas feitas com a chave atual ou anterior são aceitas, mas chaves retiradas não podem voltar.

    ## Resultado esperado

    Investigue a aplicação, localize a responsabilidade correta e implemente uma solução determinística para **gestão de segredos**. O contrato público e o comportamento já existente fora desse fluxo devem ser preservados.

    Regras de aceitação do domínio:

        - chave atual vale.
    - chave anterior vale na janela.
    - chave antiga demais falha.
    - anterior vazia não aceita vazio.
    - comparação é exata.

    O teste público demonstra o formato mínimo: a entrada `k2|k2|k1` produz `valid`. Os testes privados variam valores, ordem e limites dentro das mesmas regras.

    ## Restrições

    Não reduza a base a uma função paralela, não codifique somente os exemplos públicos e não introduza serviços externos. Acrescente testes de regressão no nível adequado.

    ## Entrega

    Execute os scripts fornecidos e entregue o repositório completo. Os testes privados exercitam casos de borda não expostos no enunciado.
