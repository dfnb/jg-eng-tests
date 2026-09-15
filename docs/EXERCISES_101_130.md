# Catálogo dos exercícios 101–130

Todos os itens desta faixa usam o perfil `small-production`; o aluno precisa navegar por uma base ampla antes de alterar o comportamento focal.

| ID | Exercício | Área | Stack | Competência focal |
| --- | --- | --- | --- | --- |
| 101 | Fluxo de aprovação de compras | Backend | .NET 10 / C# | workflow de domínio |
| 102 | Estorno no razão contábil | Backend | .NET 10 / C# | invariantes contábeis |
| 103 | Precedência de configuração regional | Backend | .NET 10 / C# | configuração |
| 104 | Reconstrução de histórico de auditoria | Backend | .NET 10 / C# | dados temporais |
| 105 | Alocação de remessas | Backend | .NET 10 / C# | algoritmos de domínio |
| 106 | Agrupamento de notificações | Backend | .NET 10 / C# | processamento em lote |
| 107 | Retenção com bloqueio legal | Backend | .NET 10 / C# | compliance |
| 108 | Rotação de segredo sem indisponibilidade | Backend | .NET 10 / C# | gestão de segredos |
| 109 | Readiness de dependências | Backend | .NET 10 / C# | observabilidade |
| 110 | Rollout percentual de feature | Backend | .NET 10 / C# | entrega progressiva |
| 111 | Encerramento gracioso de workers | Backend | .NET 10 / C# | lifecycle |
| 112 | Fan-out paralelo ordenado | Backend | .NET 10 / C# | concorrência |
| 113 | Descontinuação de API | Backend | .NET 10 / C# | governança de API |
| 114 | Privacidade em baggage de tracing | Backend | .NET 10 / C# | telemetria |
| 115 | Classificação de retry de banco | Backend | .NET 10 / C# | persistência resiliente |
| 116 | Navegação orientada por permissões | Frontend | React / TypeScript | autorização de interface |
| 117 | Histórico de undo e redo | Frontend | Angular / TypeScript | estado reversível |
| 118 | Autosave versionado | Frontend | React / TypeScript | persistência de rascunho |
| 119 | Restauração de wizard | Frontend | Angular / TypeScript | formulários multietapa |
| 120 | Resumo acessível de gráfico | Frontend | React / TypeScript | visualização acessível |
| 121 | Preferência por movimento reduzido | Frontend | Angular / TypeScript | acessibilidade visual |
| 122 | Entrada decimal localizada | Frontend | React / TypeScript | internacionalização |
| 123 | Identidade estável em formulários | Frontend | Angular / TypeScript | formulários dinâmicos |
| 124 | Cache normalizado de entidades | Frontend | React / TypeScript | gerenciamento de estado |
| 125 | Paridade de feature flags no SSR | Frontend | Angular / TypeScript | renderização híbrida |
| 126 | Ordenação de chunks em streaming | Frontend | React / TypeScript | renderização incremental |
| 127 | Evicção por quota do navegador | Frontend | Angular / TypeScript | armazenamento local |
| 128 | Fallback de área de transferência | Frontend | React / TypeScript | integração com navegador |
| 129 | Paginação para impressão | Frontend | Angular / TypeScript | mídia impressa |
| 130 | Contrato de eventos entre microfrontends | Frontend | React / TypeScript | arquitetura frontend |

## 101 — Fluxo de aprovação de compras

Uma plataforma de compras precisa decidir a próxima etapa usando valor, centro de custo e segregação de funções.

- **Foco:** workflow de domínio
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): compra pequena é aprovada.
  - C02 (mínimo): valor médio exige gerente.
  - C03 (mínimo): alto valor exige diretor.
  - C04 (intermediário): sem orçamento rejeita.
  - C05 (desejado): autor não aprova a própria compra.

## 102 — Estorno no razão contábil

Um estorno deve produzir lançamentos de sinal oposto, na moeda original, sem alterar o lançamento histórico.

- **Foco:** invariantes contábeis
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): débito vira crédito.
  - C02 (mínimo): crédito vira débito.
  - C03 (mínimo): centavos são preservados.
  - C04 (intermediário): valor não muda de sinal.
  - C05 (desejado): moeda é normalizada.

## 103 — Precedência de configuração regional

A aplicação combina configuração global, regional e de tenant sem deixar valor vazio sobrescrever uma configuração válida.

- **Foco:** configuração
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): tenant vence.
  - C02 (mínimo): regional cobre tenant vazio.
  - C03 (mínimo): global é fallback.
  - C04 (intermediário): espaço não sobrescreve.
  - C05 (desejado): tudo ausente é unset.

## 104 — Reconstrução de histórico de auditoria

Consultas históricas precisam reconstruir o valor vigente em um instante, mesmo quando eventos chegam fora de ordem.

- **Foco:** dados temporais
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): usa último evento anterior.
  - C02 (mínimo): ordena eventos recebidos fora de ordem.
  - C03 (mínimo): antes da criação é ausente.
  - C04 (intermediário): evento na borda vale.
  - C05 (desejado): sem eventos é ausente.

## 105 — Alocação de remessas

Pedidos devem ser alocados ao depósito com estoque suficiente e menor distância, usando ID como desempate estável.

- **Foco:** algoritmos de domínio
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): menor distância vence.
  - C02 (mínimo): estoque insuficiente é ignorado.
  - C03 (mínimo): ID desempata.
  - C04 (intermediário): nenhum candidato.
  - C05 (desejado): lista vazia.

## 106 — Agrupamento de notificações

Um job de digest agrupa notificações por destinatário e canal, remove duplicatas e preserva ordem determinística.

- **Foco:** processamento em lote
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): agrupa em ordem estável.
  - C02 (mínimo): remove duplicata.
  - C03 (mínimo): canais ficam separados.
  - C04 (intermediário): destinatários ficam separados.
  - C05 (desejado): vazio produz vazio.

## 107 — Retenção com bloqueio legal

A limpeza de documentos deve respeitar prazo, bloqueio legal e estado de exclusão já concluída.

- **Foco:** compliance
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): expirado é removido.
  - C02 (mínimo): novo é mantido.
  - C03 (mínimo): hold prevalece.
  - C04 (intermediário): já removido é ignorado.
  - C05 (desejado): um dia antes mantém.

## 108 — Rotação de segredo sem indisponibilidade

Durante uma rotação, assinaturas feitas com a chave atual ou anterior são aceitas, mas chaves retiradas não podem voltar.

- **Foco:** gestão de segredos
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): chave atual vale.
  - C02 (mínimo): chave anterior vale na janela.
  - C03 (mínimo): chave antiga demais falha.
  - C04 (intermediário): anterior vazia não aceita vazio.
  - C05 (desejado): comparação é exata.

## 109 — Readiness de dependências

O endpoint de readiness deve distinguir dependências obrigatórias das opcionais e não confundir liveness com prontidão.

- **Foco:** observabilidade
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): todas obrigatórias disponíveis.
  - C02 (mínimo): banco indisponível bloqueia.
  - C03 (mínimo): opcional não bloqueia.
  - C04 (intermediário): sem dependências obrigatórias.
  - C05 (desejado): lista vazia.

## 110 — Rollout percentual de feature

Uma feature deve ser atribuída de forma determinística por usuário, respeitando percentuais zero e cem.

- **Foco:** entrega progressiva
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): zero desliga.
  - C02 (mínimo): cem liga.
  - C03 (mínimo): bucket abaixo liga.
  - C04 (intermediário): bucket na borda desliga.
  - C05 (desejado): mesmo usuário é estável.

## 111 — Encerramento gracioso de workers

Ao receber shutdown, o worker para de aceitar itens e aguarda somente o trabalho em andamento até o prazo.

- **Foco:** lifecycle
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): trabalho ativo drena.
  - C02 (mínimo): prazo encerra à força.
  - C03 (mínimo): fila não é iniciada.
  - C04 (intermediário): sem trabalho para.
  - C05 (desejado): ativo ignora fila nova.

## 112 — Fan-out paralelo ordenado

Resultados de chamadas paralelas precisam manter a ordem de entrada e registrar falhas por item sem abortar o lote.

- **Foco:** concorrência
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): ordem é preservada.
  - C02 (mínimo): falha é localizada.
  - C03 (mínimo): todas falham.
  - C04 (intermediário): um item.
  - C05 (desejado): vazio.

## 113 — Descontinuação de API

Versões depreciadas devem emitir Deprecation e Sunset coerentes sem marcar versões ainda suportadas.

- **Foco:** governança de API
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): versão antiga deprecia.
  - C02 (mínimo): versão atual suporta.
  - C03 (mínimo): versão futura suporta.
  - C04 (intermediário): sunset é preservado.
  - C05 (desejado): primeira versão atual.

## 114 — Privacidade em baggage de tracing

Propagação de tracing deve manter somente chaves permitidas, limitar tamanho e ordenar a saída.

- **Foco:** telemetria
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): mantém allowlist.
  - C02 (mínimo): remove segredo.
  - C03 (mínimo): remove valor longo.
  - C04 (intermediário): ordena chaves.
  - C05 (desejado): vazio.

## 115 — Classificação de retry de banco

A camada de dados deve repetir somente deadlocks transitórios e nunca violações permanentes ou tentativas já esgotadas.

- **Foco:** persistência resiliente
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): deadlock repete.
  - C02 (mínimo): última tentativa esgota.
  - C03 (mínimo): unique não repete.
  - C04 (intermediário): timeout não é assumido.
  - C05 (desejado): zero tentativas ainda repete.

## 116 — Navegação orientada por permissões

O menu deve ocultar ações indisponíveis sem usar isso como substituto da autorização do servidor.

- **Foco:** autorização de interface
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): mostra rota permitida.
  - C02 (mínimo): oculta rota negada.
  - C03 (mínimo): múltiplas permissões.
  - C04 (intermediário): rota pública permanece.
  - C05 (desejado): lista vazia.

## 117 — Histórico de undo e redo

Um editor precisa calcular corretamente o estado após comandos, undo, redo e nova edição que invalida o futuro.

- **Foco:** estado reversível
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): undo restaura.
  - C02 (mínimo): redo reaplica.
  - C03 (mínimo): nova edição limpa redo.
  - C04 (intermediário): undo vazio é seguro.
  - C05 (desejado): vários undos.

## 118 — Autosave versionado

O autosave deve ignorar respostas antigas e distinguir conflito de versão de falha de rede.

- **Foco:** persistência de rascunho
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): resposta atual aplica.
  - C02 (mínimo): resposta antiga ignora.
  - C03 (mínimo): resposta futura ignora.
  - C04 (intermediário): conflito abre resolução.
  - C05 (desejado): rede agenda retry.

## 119 — Restauração de wizard

Um fluxo multietapa deve restaurar somente etapas válidas e nunca pular uma etapa obrigatória incompleta.

- **Foco:** formulários multietapa
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): restaura etapa válida.
  - C02 (mínimo): não pula primeira inválida.
  - C03 (mínimo): limita na inválida.
  - C04 (intermediário): todas válidas permitem fim.
  - C05 (desejado): índice negativo vira zero.

## 120 — Resumo acessível de gráfico

Um gráfico precisa produzir alternativa textual com tendência, mínimo e máximo a partir dos mesmos dados visuais.

- **Foco:** visualização acessível
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): tendência de alta.
  - C02 (mínimo): tendência de baixa.
  - C03 (mínimo): estável.
  - C04 (intermediário): um ponto.
  - C05 (desejado): sem dados.

## 121 — Preferência por movimento reduzido

Transições precisam respeitar prefers-reduced-motion mantendo feedback sem animação contínua.

- **Foco:** acessibilidade visual
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): reduce remove transição.
  - C02 (mínimo): reduce mantém progresso estático.
  - C03 (mínimo): normal anima modal.
  - C04 (intermediário): normal anima progresso.
  - C05 (desejado): efeito desconhecido respeita reduce.

## 122 — Entrada decimal localizada

Valores monetários digitados com separadores locais precisam virar representação canônica sem ambiguidades.

- **Foco:** internacionalização
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): pt-BR converte vírgula.
  - C02 (mínimo): en-US converte agrupamento.
  - C03 (mínimo): inteiro recebe centavos.
  - C04 (intermediário): texto inválido.
  - C05 (desejado): espaços são aceitos.

## 123 — Identidade estável em formulários

Linhas adicionadas e removidas devem preservar IDs estáveis para não trocar foco nem estado de validação.

- **Foco:** formulários dinâmicos
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): remove por ID.
  - C02 (mínimo): adiciona ao fim.
  - C03 (mínimo): adiciona na posição.
  - C04 (intermediário): ID duplicado não entra.
  - C05 (desejado): remoção ausente não muda.

## 124 — Cache normalizado de entidades

Atualizações parciais devem mesclar entidades por ID sem duplicar referências nas listas.

- **Foco:** gerenciamento de estado
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): atualiza entidade.
  - C02 (mínimo): insere entidade.
  - C03 (mínimo): ordena por ID.
  - C04 (intermediário): vazio aceita primeira.
  - C05 (desejado): valor vazio é mantido.

## 125 — Paridade de feature flags no SSR

Servidor e cliente precisam usar o mesmo snapshot de flags durante a hidratação para evitar reconstrução da árvore.

- **Foco:** renderização híbrida
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): snapshots iguais hidratam.
  - C02 (mínimo): ordem não importa.
  - C03 (mínimo): flag extra reconstrói.
  - C04 (intermediário): flag ausente reconstrói.
  - C05 (desejado): dois vazios hidratam.

## 126 — Ordenação de chunks em streaming

Chunks de uma resposta podem chegar fora de ordem e só devem liberar o prefixo contínuo já disponível.

- **Foco:** renderização incremental
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): primeiro chunk libera.
  - C02 (mínimo): gap aguarda.
  - C03 (mínimo): fora de ordem completa prefixo.
  - C04 (intermediário): continua de checkpoint.
  - C05 (desejado): vazio aguarda.

## 127 — Evicção por quota do navegador

O cache local deve remover entradas menos recentes até caber, preservando itens fixados.

- **Foco:** armazenamento local
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): cabe sem remover.
  - C02 (mínimo): remove mais antigo.
  - C03 (mínimo): remove até caber.
  - C04 (intermediário): fixado é preservado.
  - C05 (desejado): vazio recebe item.

## 128 — Fallback de área de transferência

A ação de copiar deve escolher API segura, fallback ou orientação manual conforme contexto e permissão.

- **Foco:** integração com navegador
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): API moderna em contexto seguro.
  - C02 (mínimo): contexto inseguro usa fallback.
  - C03 (mínimo): API ausente usa fallback.
  - C04 (intermediário): permissão negada orienta manual.
  - C05 (desejado): prompt ainda tenta API.

## 129 — Paginação para impressão

Relatórios impressos devem calcular quebras sem separar cabeçalho e primeira linha de uma seção.

- **Foco:** mídia impressa
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): uma página.
  - C02 (mínimo): quebra antes da seção.
  - C03 (mínimo): múltiplas páginas.
  - C04 (intermediário): seção do tamanho da página.
  - C05 (desejado): seção maior sinaliza.

## 130 — Contrato de eventos entre microfrontends

Eventos entre aplicações precisam validar versão, namespace e campos obrigatórios antes de atravessar a fronteira.

- **Foco:** arquitetura frontend
- **Perfil:** pequena aplicação de produção
- **Critérios discretos:**

  - C01 (mínimo): evento válido entra.
  - C02 (mínimo): namespace externo ignora.
  - C03 (mínimo): versão antiga rejeita.
  - C04 (intermediário): ID obrigatório.
  - C05 (desejado): timestamp obrigatório.
