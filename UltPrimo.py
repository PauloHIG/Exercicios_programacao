'''retornar o último primo do numero dado como parâmetro na função'''
while True:
	try:
		n = int(input('Digite um número inteiro para eu mostrar o seu ultimo número primo: '))
	except:
		print('Somente números inteiros')
		continue
	break
def UltP(n):#função ultimo primo
	while True:
		for i in range(n,0,-1):#se eu quero o ultimo primo, obviamente começo de cima pra baixo
			primo = verPrimo(i)#preferi separar em duas funções, mas não era realmente necessário
			if primo == True:
				print('{} é o último numero prímo de {}'.format(i,n))
				break
		break

def verPrimo(n):#retorna falso se o número não for primo
	cont = 0
	for i in range(1,n+1):
		if n % i == 0:
			cont +=1
		if cont == 3:#é assim que funciona, se o cont for maior que 2, o número é composto, logo, não preciso perder memoria
			break # uma vez que meu objetivo é apenas descobrir se o número é primo ou não
	if cont == 2:
		return True
	else:
		return False
UltP(n)