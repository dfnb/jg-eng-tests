# Desafio: automatizar o ambiente local

Crie scripts Bash e PowerShell equivalentes que validem ferramentas, preparem um diretório de estado, apliquem a migration fixture uma única vez e executem verificações. Eles devem funcionar a partir de qualquer diretório, propagar falhas e nunca limpar fora do estado do projeto.

Use `PROJECT_STATE_DIR` quando definido; caso contrário, use `.local-state` na raiz. Repetir setup não pode duplicar a migration. Não instale ferramentas globalmente.
