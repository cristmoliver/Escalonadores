#Variáveis global
tempo_total = 0
tempo_espera_rr = []
tempo_resposta_rr = []
tempo_retorno_rr = []

#Os processos
global num_processos
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

def insertionSort():
	for x in range(1,num_processos):
		valor_chegada =	processos[CHEGADA][x]
		valor_duracao = processos[DURACAO][x]
		indice = x

		while indice > 0 and processos[CHEGADA][indice-1] > valor_chegada:
			processos[CHEGADA][indice] = processos[CHEGADA][indice-1]
			processos[DURACAO][indice] = processos[DURACAO][indice-1]
			processos_sjf[CHEGADA][indice] = processos_sjf[CHEGADA][indice-1]
			processos_sjf[DURACAO][indice] = processos_sjf[DURACAO][indice-1]
			processos_sjf_aux[CHEGADA][indice] = processos_sjf_aux[CHEGADA][indice-1]
			processos_sjf_aux[DURACAO][indice] = processos_sjf_aux[DURACAO][indice-1]
			indice = indice-1
			pass
		processos[CHEGADA][indice] = valor_chegada
		processos[DURACAO][indice] = valor_duracao
		processos_sjf[CHEGADA][indice] = valor_chegada
		processos_sjf[DURACAO][indice] = valor_duracao
		processos_sjf_aux[CHEGADA][indice] = valor_chegada
		processos_sjf_aux[DURACAO][indice] = valor_duracao
		pass
	pass

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
		i+=processos_sjf[DURACAO][j]
		if processos_sjf_aux[DURACAO][menor] != -1:
			processos_sjf[DURACAO][j] = processos_sjf_aux[DURACAO][menor]
			processos_sjf[CHEGADA][j] = processos_sjf_aux[CHEGADA][menor]
			
			processos_sjf_aux[DURACAO][menor] = processos_sjf_aux[DURACAO][j]
			processos_sjf_aux[CHEGADA][menor] = processos_sjf_aux[CHEGADA][j]

			processos_sjf_aux[DURACAO][j] = -1
			processos_sjf_aux[CHEGADA][j] = -1
			j+=1
			pass
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
	print('FCFS', round(tempo_med_retorno,1), round(tempo_med_resposta,1), round(tempo_med_espera,1))
	pass

#SJF
def sjf():
	sjfOrder()
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	tempo_espera = 0
	tempo_retorno = 0
	tempo_resposta = 0
	global tempo_total
	tempo_total = 0

	for x in range(num_processos):
		if tempo_total < processos_sjf[CHEGADA][x]:
			while tempo_total < processos_sjf[CHEGADA][x]:
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
	print('SJF', round(tempo_med_retorno,1), round(tempo_med_resposta,1), round(tempo_med_espera,1))
	pass

def rr():
	tempo_med_retorno = 0
	tempo_med_resposta = 0
	tempo_med_espera = 0
	global tempo_total
	global tempo_resposta_rr
	tempo_total = 0
	fim = 0
	fila = []
	quantum = 2
	primeiro = -1

	chegada_inicial = []
	for x in range(num_processos):
		chegada_inicial.append(processos[CHEGADA][x])
		pass
	#print(len(fila))
	while fim < num_processos:
		for x in range(num_processos):
			if processos[CHEGADA][x] <= tempo_total and processos[CHEGADA][x] != -1 and x != primeiro:
				if len(fila) == 0:
					fila.append(x)
					pass
				else:
					num	= 0
					for y in range(len(fila)):
						if fila[y] == x:
							num = 0
							break
							pass
						num = 1
						pass
					if num ==  1:
						fila.append(x)
						pass
				pass	
			pass
		if primeiro != -1:
			if processos[CHEGADA][primeiro] <= tempo_total and processos[CHEGADA][primeiro] != -1:
				fila.append(primeiro)
				pass
			pass
		if len(fila) == 0:
			tempo_total+=1
			continue
			pass
		primeiro = fila[0]

		tempo_espera_rr[primeiro] += tempo_total - processos[CHEGADA][primeiro]
		if tempo_resposta_rr[primeiro] == -1:
			tempo_resposta_rr[primeiro] = tempo_total - processos[CHEGADA][primeiro]
			pass
		cont = 0
		while processos[DURACAO][primeiro] != 0:
			cont+=1
			tempo_total+=1
			processos[DURACAO][primeiro] = processos[DURACAO][primeiro] - 1
			if  cont == 2:
				break
				pass
			pass
		processos[CHEGADA][primeiro] = tempo_total
		if processos[DURACAO][primeiro] == 0:
			tempo_retorno_rr[primeiro] = tempo_total - chegada_inicial[primeiro]
			fim+=1
			processos[CHEGADA][primeiro] = -1
			pass
		del fila[0]
		pass

	for x in range(num_processos):
		tempo_med_resposta += tempo_resposta_rr[x]
		tempo_med_retorno += tempo_retorno_rr[x]
		tempo_med_espera += tempo_espera_rr[x]
		pass	
	tempo_med_espera = tempo_med_espera / num_processos
	tempo_med_retorno = tempo_med_retorno / num_processos
	tempo_med_resposta = tempo_med_resposta / num_processos
	print('RR', round(tempo_med_retorno,1), round(tempo_med_resposta,1), round(tempo_med_espera,1))

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
    tempo_retorno_rr.append(0)
    tempo_resposta_rr.append(-1)
    tempo_espera_rr.append(0)
    #num_processos += 1
ref_arquivo.close()
#print(processos_sjf)
num_processos = len(processos[0])

insertionSort()

fcfs()
sjf()
rr()