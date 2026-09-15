# Avaliação: Scripts de desenvolvimento

| ID | Nível | Peso | Condição |
| --- | --- | ---: | --- |
| C01 | mínimo | 3 | setup funciona fora da raiz |
| C02 | mínimo | 2 | segunda execução não duplica migration |
| C03 | mínimo | 2 | falhas e caminhos usam quoting/modo estrito |
| C04 | intermediário | 2 | reset recusa diretório inseguro |
| C05 | desejado | 1 | PowerShell oferece o mesmo contrato |

Armadilhas: depender de `pwd`, ignorar exit codes e usar remoção ampla. O grader executa em cópia temporária e nunca aponta a limpeza para dados reais.
