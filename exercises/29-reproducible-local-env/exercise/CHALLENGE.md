# Desafio: ambiente local reproduzível

Complete `compose.yaml` e os Dockerfiles para que `docker compose up --build` inicie API, worker, PostgreSQL e Redis. A API só deve iniciar após dependências saudáveis, dados devem persistir em volume nomeado, portas devem ser configuráveis e processos da aplicação não devem rodar como root.
