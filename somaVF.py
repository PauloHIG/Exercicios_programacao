#mathgame
#a idéia é clonar um jogo de celular em que você vê uma soma de um número e o resultado, e verifica se o resultado está certo ou errado com limite de tempo
from random import randint
recordeSoma = 0
def jogada():
	while True:#mais um try para o usuario digitar o que é pedido sem interromper o programa
		try:
			resposta = input('V(verdadeiro) ou F(falso)\n')
		except:
			print('Somente V ou F')
			continue
		if resposta.upper() not in ('V F'):
			print('Somente V ou F')
			continue
		break
	return resposta
def jogo():
	contaAcertos = 0
	global recordeSoma
	while True:
		n1 = randint(1,10)
		n2 = randint(1,10)
		dec = randint(0,1)#uma tentativa de fazer com que 50% das respostas seja a certa
		ref=0

		if dec == 1:#caso seja 0, a resposta não será alterada, se mantendo verdadeira
			#resposta que poderá ser verdadeira ou falsa se for igual a soma de n1 + n2
			ref = randint(-2,2)

		if n1+n2 == n1+n2+ref:
			certo = 'V'
		else:
			certo = 'F'
		print('pontuação atual: {} recorde:{}'.format(contaAcertos,recordeSoma))
		print('Esta conta está certa?')
		print('{} + {} = {}'.format(n1,n2,n1+n2+ref))
		resposta = jogada()
		if resposta.upper() != certo:
			print('você errou, fim de jogo')
			break
		else:
			contaAcertos += 1
		if contaAcertos > recordeSoma:
			recordeSoma = contaAcertos
while True:
	jogo()
	continuar = input('Você quer continuar jogando? aperte qualquer tecla para continuar ou N para sair')
	if continuar.upper() == 'N':
		print('Saindo do jogo')
		break