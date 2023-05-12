#mathgame
#a idéia é clonar um jogo de celular em que você vê uma soma de um número e o resultado, e verifica se o resultado está certo ou errado com limite de tempo
from random import randint
import sys

recordeSoma = 0
recordeSub  = 0
recordeMulti = 0
recordeDiv = 0

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

def escolha():
	while True:
		try:
			escolha = int(input(""))
		except:
			print('Somente as opções de 1 a 5')
			continue
		if escolha not in (1,2,3,4,5):
			print('Somente as opções de 1 a 5')
			continue
		break
	return escolha

def jogoSoma():
	contaAcertos = 0
	global recordeSoma
	while True:
		n1 = randint(1,10)
		n2 = randint(1,10)
		dec = randint(0,1)#uma tentativa de fazer com que 50% das respostas seja a certa
		ref=0

		if dec == 1:#caso seja 0, a resposta não será alterada, se mantendo verdadeira
			#resposta que poderá ser verdadeira ou falsa se for igual a soma de n1 + n2
			ref = randint(0,4)

		if n1+n2 == n1+n2+ref:
			certo = 'V'
		else:
			certo = 'F'
		print('pontuação atual: {} recorde:{}'.format(contaAcertos,recordeSoma))#o récorde ainda não é gravado corretamente, ele desaparece quando o programa é fechado
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
def jogoSub():
	contaAcertos = 0
	global recordeSub
	while True:
		n1 = randint(1,10)
		n2 = randint(1,10)
		dec = randint(0,1)#uma tentativa de fazer com que 50% das respostas seja a certa
		ref=0

		if dec == 1:
			ref = randint(0,4)#o ref é a variável que decide se a conta vai ficar verdadeira ou falsa
		if n1-n2 == n1-n2+ref:
			certo = 'V'
		else:
			certo = 'F'
		print('pontuação atual: {} recorde:{}'.format(contaAcertos,recordeSub))#o récorde ainda não é gravado corretamente, ele desaparece quando o programa é fechado
		print('Esta conta está certa?')
		print('{} - {} = {}'.format(n1,n2,n1-n2+ref))
		resposta = jogada()
		if resposta.upper() != certo:
			print('você errou, fim de jogo')
			break
		else:
			contaAcertos += 1
		if contaAcertos > recordeSub:
			recordeSub = contaAcertos
def jogoMulti():
	contaAcertos = 0
	global recordeMulti
	while True:
		n1 = randint(1,10)
		n2 = randint(1,10)
		dec = randint(0,1)#uma tentativa de fazer com que 50% das respostas seja a certa
		ref=0

		if dec == 1:
			ref = randint(0,4)#o ref é a variável que decide se a conta vai ficar verdadeira ou falsa
		if n1*n2 == (n1*n2)+ref:
			certo = 'V'
		else:
			certo = 'F'
		print('pontuação atual: {} recorde:{}'.format(contaAcertos,recordeMulti))#o récorde ainda não é gravado corretamente, ele desaparece quando o programa é fechado
		print('Esta conta está certa?')
		print('{} * {} = {}'.format(n1,n2,(n1*n2)+ref))
		resposta = jogada()
		if resposta.upper() != certo:
			print('você errou, fim de jogo')
			break
		else:
			contaAcertos += 1
		if contaAcertos > recordeMulti:
			recordeMulti = contaAcertos
def jogoDiv():
	contaAcertos = 0
	global recordeDiv #TO DO, usar variável global não é um boa pratica
	while True:
		n1 = randint(1,10)
		n2 = randint(1,10)
		dec = randint(0,1)#uma tentativa de fazer com que 50% das respostas seja a certa
		ref=0

		if dec == 1:
			ref = randint(0,4)#o ref é a variável que decide se a conta vai ficar verdadeira ou falsa
		if n1/n2 == (n1//n2)+ref:
			certo = 'V'
		else:
			certo = 'F'
		print('pontuação atual: {} recorde:{}'.format(contaAcertos,recordeDiv))#o récorde ainda não é gravado corretamente, ele desaparece quando o programa é fechado
		print('Esta conta está certa?')
		print('{} / {} = {}'.format(n1,n2,(n1//n2)+ref))
		resposta = jogada()
		if resposta.upper() != certo:
			print('você errou, fim de jogo')
			break
		else:
			contaAcertos += 1
		if contaAcertos > recordeDiv:
			recordeDiv = contaAcertos

while True:
	print('------Jogo de Matemática-------')
	print('Recordes: Soma = {}, Subtração = {}, Multiplicação = {}, Divisão = {}'.format(recordeSoma, recordeSub, recordeMulti, recordeDiv))
	print('Escolha uma operação')
	print('1-Soma')
	print('2-Subtração')
	print('3-multiplicação')
	print('4-divisão')
	print('5-sair')

	op = escolha()
	dic_opcoes = {1:jogoSoma,2:jogoSub,3:jogoMulti,4:jogoDiv}
	if op == 5:
		print('Saindo do programa...')
		sys.exit()
		break
	dic_opcoes[op]()
