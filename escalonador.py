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
processos_sjf =[]
processos_sjf.append([])
processos_sjf.append([])
processos_sjf_aux =[]
processos_sjf_aux.append([])
processos_sjf_aux.append([])
#Chegada e Duração CONSTANTES NÃO ALTERAR
CHEGADA = 0
DURACAO = 1

#ordernar para pegar o menor tempo de duração dos processos para o SJF
def sjfOrder():
	global processos_sjf
	i = 0
	j = 0
	aux = []
	menor = 0
	cont = 0 #Cont é o número de processos que estão na fila de prontos em um determinado tempo
	while i <= tempo_total:
		for x in range(j, num_processos):
			if i >= processos_sjf_aux[CHEGADA][x] and processos_sjf_aux[CHEGADA][x] != -1:
				cont+=1
				aux.append(x)
				pass
			pass
		for h in range(1, cont):
			if (processos_sjf_aux[DURACAO][aux[h-1]] > processos_sjf_aux[DURACAO][aux[h]]):
				menor = aux[h]
				maior = aux[h-1]
				pass
			else:
				maior = aux[h]
				pass
			pass
		if j == num_processos:
			break
			pass

		if processos_sjf_aux[DURACAO][menor] != -1:
			processos_sjf[DURACAO][j] = processos_sjf_aux[DURACAO][menor]
			processos_sjf[CHEGADA][j] = processos_sjf_aux[CHEGADA][menor]
			
			processos_sjf_aux[DURACAO][menor] = processos_sjf_aux[DURACAO][j]
			processos_sjf_aux[CHEGADA][menor] = processos_sjf_aux[CHEGADA][j]

			processos_sjf_aux[DURACAO][j] = -1
			processos_sjf_aux[CHEGADA][j] = -1
			j+=1
			pass
		#i+=processos_sjf[DURACAO][j]
		i+=1
		cont = 0
		aux = []
		pass
	pass

#FCFS
def fcfs():
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	global tempo_total
	for x in range(num_processos):
		if tempo_total < processos[CHEGADA][x]:
			while tempo_total < processos[CHEGADA][x]:
				tempo_total+=1
				pass
			pass
		tempo_espera = tempo_total - processos[CHEGADA][x] #cálculo do tempo de espera
		tempo_med_espera += tempo_espera #adicionando para fazer a média no final
		tempo_resposta = tempo_espera
		tempo_med_resposta += tempo_resposta
		cont = 0
		while cont < processos[DURACAO][x]:
			cont+=1
			tempo_total+=1
			pass
		#print(cont)
		tempo_retorno = tempo_total - processos[CHEGADA][x]
		tempo_med_retorno += tempo_retorno
		pass
	tempo_med_resposta = tempo_med_resposta / num_processos
	tempo_med_espera = tempo_med_espera / num_processos
	tempo_med_retorno = tempo_med_retorno / num_processos
	print('FCFS', tempo_med_retorno, tempo_med_resposta, tempo_med_espera)
	pass

#SJF
def sjf():
	sjfOrder()
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	global tempo_total
	tempo_total = 0
	for x in range(num_processos):
		if tempo_total < processos[CHEGADA][x]:
			while tempo_total < processos[CHEGADA][x]:
				tempo_total+=1
				pass
			pass
		tempo_espera = tempo_total - processos_sjf[CHEGADA][x] #cálculo do tempo de espera
		tempo_med_espera += tempo_espera #adicionando para fazer a média no final
		tempo_resposta = tempo_espera
		tempo_med_resposta += tempo_resposta
		cont = 0
		while cont < processos_sjf[DURACAO][x]:
			cont+=1
			tempo_total+=1
			pass
		#print(cont)
		tempo_retorno = tempo_total - processos_sjf[CHEGADA][x]
		tempo_med_retorno += tempo_retorno
		pass
	tempo_med_resposta = tempo_med_resposta / num_processos
	tempo_med_espera = tempo_med_espera / num_processos
	tempo_med_retorno = tempo_med_retorno / num_processos
	print('SJF', tempo_med_retorno, tempo_med_resposta, tempo_med_espera)

	pass

#Corpo principal
#Lendo o arquivo de instâncias para pegar os processos
ref_arquivo = open("instancias.txt","r")

for linha in ref_arquivo:
    valores = linha.split()
    #print('P',num_processos, ' ', 'tempo de chegada: ', valores[0], 'duração de cada processo: ', valores[1])
    processos[CHEGADA].append(int(valores[CHEGADA])) 
    processos[DURACAO].append(int(valores[DURACAO]))
    processos_sjf[CHEGADA].append(int(valores[CHEGADA])) 
    processos_sjf[DURACAO].append(int(valores[DURACAO]))
    processos_sjf_aux[CHEGADA].append(int(valores[CHEGADA])) 
    processos_sjf_aux[DURACAO].append(int(valores[DURACAO]))
    num_processos += 1
ref_arquivo.close()
#print(processos_sjf)

fcfs()
sjf()