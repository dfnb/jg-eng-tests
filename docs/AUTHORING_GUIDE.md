# Guia para criação de exercícios

## Processo

1. Escolher uma competência principal e no máximo duas secundárias.
2. Escrever primeiro os critérios discretos e como serão comprovados.
3. Criar a solução de referência e os testes privados.
4. Derivar o exercício removendo ou alterando somente o ponto avaliado.
5. Escrever README e desafio depois que os comandos estiverem estáveis.
6. Validar estados intacto, resolvido, mutantes e solução alternativa.
7. Fazer revisão pedagógica e técnica por outra pessoa.
8. Empacotar apenas o diretório `exercise/` e testar o pacote limpo.

Escrever a avaliação antes do enunciado ajuda a impedir requisitos vagos e desafios impossíveis de corrigir objetivamente.

## Como escrever o desafio

O `CHALLENGE.md` deve responder:

- qual problema do produto ou da equipe precisa ser resolvido;
- qual comportamento final é esperado;
- quais interfaces públicas não podem mudar;
- quais casos são exemplos ilustrativos, sem enumerar todos os testes;
- como executar e entregar a solução;
- o que está fora de escopo.

Ele não deve indicar arquivo, linha, classe, padrão ou causa raiz, salvo quando localizar o trabalho fizer parte explícita do pedido realista.

## Dosagem da investigação

O estudante deve conseguir distinguir o problema principal em até 20–30% do tempo estimado. Se descobrir o ponto relevante consome quase todo o exercício, a tarefa está medindo busca aleatória. Se o enunciado aponta diretamente a linha e a correção, não há investigação.

Pistas legítimas incluem logs, teste falhando, relato reproduzível, métrica e contrato de API. Falsos caminhos só são usados quando refletem ruído plausível e não exigem adivinhação.

## Repositório realista, mas focado

- inclua duas ou três camadas apenas quando elas ajudarem o cenário;
- forneça integrações locais ou simuladas já configuradas;
- mantenha código não relacionado consistente e coberto por testes;
- evite TODOs que denunciem a resposta;
- evite erros de lint não relacionados;
- use dados e nomes de domínio coerentes;
- limite o diff ideal ao que uma pequena tarefa profissional exigiria.

## Bugs

Em exercícios de diagnóstico, deve existir uma causa raiz principal. Sintomas secundários podem existir, mas não devem exigir correções independentes não documentadas. O exercício intacto precisa reproduzir o erro de modo determinístico ou com um harness confiável.

## Performance

Registre baseline e alvo em hardware/ambiente controlado. Prefira medir complexidade, alocações, quantidade de consultas, payload ou chamadas externas. Quando usar tempo, execute aquecimento e várias amostras com margem suficiente.

## Segurança

Use apenas dados sintéticos e serviços locais. O desafio nunca pede exploração de alvo real. Testes devem verificar o controle corrigido, não ensinar payloads desnecessariamente perigosos no material público.

## Frontend

Forneça design ou especificação visual dentro do repositório, assets locais, API fake/real pronta e viewport alvo. A avaliação deve separar fidelidade funcional, responsividade e acessibilidade. Comparação de screenshot, quando usada, terá tolerância e não será o único critério.

## Checklist de publicação

- [ ] O exercício limpo instala e inicia seguindo apenas o README.
- [ ] O desafio cabe na duração declarada.
- [ ] Somente a competência desejada está incompleta.
- [ ] Todos os critérios são binários e possuem verificação.
- [ ] O estado intacto falha nos critérios esperados.
- [ ] A solução de referência passa em tudo.
- [ ] Uma solução alternativa razoável também passa.
- [ ] Testes não dependem de ordem, rede ou relógio real.
- [ ] Não existem segredos, dados pessoais ou licenças incompatíveis.
- [ ] O pacote do estudante não contém arquivos do avaliador.
