#Jogo da Velha
#feito para ser usado no terminal do windows, esse coloca cores nos números
import colorama
from colorama import init
from termcolor import colored
init()
def verLinhaColuna(lista:list):
	for linha in lista:
		if linha ==['X','X','X']:
			return 'X'
		elif linha==['O','O','O']:
			return 'O'
	#não consegui fazer o mesmo para a coluna, acabei tendo que fazer as comparações if por if
	for i in range(3):
		if lista[0][i] == 'X' and lista[0][i] == lista[1][i] and lista[1][i] == lista[2][i] and lista[0][i] == lista[2][i]:
			return 'X'
		elif lista[0][i] == 'O' and lista[0][i] == lista[1][i] and lista[1][i] == lista[2][i] and lista[0][i] == lista[2][i]:
			return 'O'
def verDiagonal(lista:list):
	conty=0
	contx=0
	for i in range(3):
		if lista[i][i] == 'O':
			conty+=1
		elif lista[i][i]=='X':
			contx+=1
	if contx ==3:
		return 'X'
	elif conty ==3:
		return 'O'
def verDiagonal2(lista:list):
	contx=0
	conty=0
	j=2
	for i in range(3):#i diminui e j aumenta, dessa forma i+j sempre vai ser igual a 2
		if lista[i][j] == 'X':
			contx+=1
		if lista[i][j] == 'O':
			conty+=1
		j-=1
	if contx ==3:
		return 'X'
	elif conty ==3:
		return 'O'
def verVelha(lista:list):
	resto = 0
	for i in range(3):
		for j in range(3):
			if type(lista[i][j])==int:
				resto += 1
	if resto == 0:
		return 'Ninguém'
def verTudo(lista:list):
	msg=None
	if msg == None:
		msg = verLinhaColuna(lista)
		if msg == None:
			msg = verDiagonal(lista)
			if msg == None:
				msg = verDiagonal2(lista)
				if msg == None:
					msg = verVelha(lista)#essa função deve ser sempre a ultima, pois ele entenda que um tabuleiro completamente preenchido é empate, mesmo se alguem tiver vencido
	return msg
def insereJogada(lista:list,jogada):
	cor=''
	if jogada == 'X':
		cor = 'cyan'
	elif jogada == 'O':
		cor = 'green'
	while True:
		#esse código aqui é para garantir que os jogadores só digitem números e 1 a 9 sem interromper o programa 
		while True:
			try:
				print('Escolha a posição para colocar ',colored(jogada,cor), '(1-9): ')
				pos = int(input(' '))#verifica se o valor é inteiro,
			except:
				print('Somente números de 1 a 9')
				continue #não permite que o código continue executando mesmo com o erro em um loop, o que faz isso é o pass
			if pos<1 or pos>9:
				print('Somente números de 1 a 9')
				continue#o contiue executa o loop do while do inicio, ignorando o codigo que está abaixo
			break#"quebra" o loop infinito, não é executado caso aconteça uma excessão por causa do continue alí em cuma
		#não consegui pensar em outra maneira de converter os números de 1 a 9 para as posições da matriz
		if pos==1:
			i=2
			j=0
		elif pos==2:
			i=2
			j=1
		elif pos==3:
			i=2
			j=2
		elif pos==7:
			i=0
			j=0
		elif pos==8:
			i=0
			j=1
		elif pos==9:
			i=0
			j=2
		elif pos==4:
			i=1
			j=0
		elif pos==5:
			i=1
			j=1
		elif pos==6:
			i=1
			j=2
		if type(lista[i][j])==int:
			lista[i][j] = jogada
			break
		else:
				print('Posição já preenchida')
def exibir(lista:list):
	cor='white'
	for linhas in lista:
			for colunas in linhas:
				if colunas=='X':
					cor='cyan'
				elif colunas=='O':
					cor='green'
				else:
					cor='white'
				print('|',colored(colunas,cor),'|',end='')
			print('')
#criação do Tabuleiro e das variáveis
tabuleiro = [[7,8,9],[4,5,6],[1,2,3]]#a ordem do tabuleiro pode parecer estranha, mas fica fácil olhar para o teclado e jogar com os números nessa ordem
msg = None
vez = 'X'#sempre vai começar com X, o jogo alterna de acordo com quem fez a ultima jogada, geralmente o vencedor ou o que começou caso dê empate
pontX=0
pontO=0
#loop do jogo
while True:
	print('Começa com {}'.format(vez))
	while msg==None:
		exibir(tabuleiro)
		insereJogada(tabuleiro,vez)
		if vez == 'X':
			vez = 'O'
		else:
			vez ='X'
		msg=verTudo(tabuleiro)
	#mensagens caso uma partida termine
	if msg=='X':
		pontX+=1
		print('',colored(msg,'cyan'),' venceu!')
	elif msg=='O':
		pontO+=1
		print('',colored(msg,'green'),' venceu!')
	else:
		print(colored('Velha!','red'))
	exibir(tabuleiro)
	print('Placar: \nX:{} O:{}'.format(pontX,pontO))
	#decisão para continuar no loop
	escolha=input('Aperte qualquer tecla pra continuar ou N pra sair: ')
	if escolha.lower() == 'n':
		print('Saindo...')
		break
	else:
		tabuleiro = [[7,8,9],[4,5,6],[1,2,3]]
		msg=None