#Variáveis global
#Os tempos
tempo_retorno = 0
tempo_resposta = 0
tempo_espera = 0
tempo_med_retorno = 0
tempo_med_resposta = 0
tempo_med_espera = 0
tempo_total = 0

#Os processos
num_processos = 0
processos = []
processos.append([])
processos.append([])

#FCFS
def fcfs():
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	tempo_total = 0
	for x in range(num_processos):
		tempo_espera = tempo_total - processos[0][x] #cálculo do tempo de espera
		tempo_med_espera += tempo_espera #adicionando para fazer a média no final
		tempo_resposta = tempo_espera
		tempo_med_resposta += tempo_resposta
		cont = 0
		while cont < processos[1][x]:
			cont+=1
			tempo_total+=1
			pass
		#print(cont)
		tempo_retorno = tempo_total - processos[0][x]
		tempo_med_retorno += tempo_retorno
		pass
	tempo_med_resposta = tempo_med_resposta / num_processos
	tempo_med_espera = tempo_med_espera / num_processos
	tempo_med_retorno = tempo_med_retorno / num_processos
	print('FCFS', tempo_med_retorno, tempo_med_resposta, tempo_med_espera)
	pass

#SJF
def sjf():
	
	pass

#Corpo principal
#Lendo o arquivo de instâncias para pegar os processos
ref_arquivo = open("instancias.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    #print('P',num_processos, ' ', 'tempo de chegada: ', valores[0], 'duração de cada processo: ', valores[1])
    processos[0].append(int(valores[0])) 
    processos[1].append(int(valores[1]))
    num_processos += 1
ref_arquivo.close()

#print(num_processos)

fcfs()