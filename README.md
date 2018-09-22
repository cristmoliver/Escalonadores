# Escalonadores de Processo
Neste projeto foi implementado um conjunto de algoritmos
de escalonamento de CPU em **Python 3.7**

Os algoritmos de escalonamento que foram 
implementados são os seguintes:
* FCFS: First-Come, First-Served
* SJF: Shortest Job First
* RR: Round Robin (com quantum = 2)

A entrada é composta por uma série de pares de
números inteiros separados por um espaço em
branco indicando o tempo de chegada e a
duração de cada processo. A entrada termina com
o fim do arquivo. Caso queira alterar a entrada, 
mude no arquivo **instancias.txt**, por exemplo:

```
0 20
0 10
4 6
4 8
```

A saída é composta por linhas contendo a sigla de
cada um dos três algoritmos e os valores médios (com uma casa decimal) para
tempo de retorno, tempo de resposta e tempo de
espera, exatamente nesta ordem, por exemplo:

```
FCFS 30,5 19,5 19,5
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
```

Para compilar apenas execute o comando no seu terminal:
>python escalonadores.py
