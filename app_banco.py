from datetime import datetime

saldo = 90.00
operacoes = ''
contLim = 0 #só pode haver 3 saques por dia

def recebeNumero(texto='numero: '):
	while True:
		try:
			dinheiro = float(input(texto))
		except ValueError:
			print('Somente Valores numericos')
			continue
		if dinheiro<0.01:
			print('O limite mínimo de para qualquer operação no banco é de R$ 0.01')
			continue
		break
	return dinheiro
def depositar():
	global saldo,operacoes
	deposito = recebeNumero('Digite o valor que quer depositar: ')
	saldo = saldo+deposito
	print('Deposito realizado com sucesso')
	#informações para o extrato
	operacoes += f'+ R$ {deposito:.2f}\n'
def sacar():
	global saldo,operacoes,contLim
	saque = recebeNumero('Digite o valor que quer sacar: ')
	if saque>saldo:
		print('!!!!!Você não possui essa quantidade de dinheiro pra sacar!!!!')
	elif saque>500:
		print('!!!!!O limite é de R$ 500.00 por saque!!!!')
	else:
		saldo = saldo-saque
		contLim+=1
		print('Saque realizado com sucesso')
		#informações para o extrato
		operacoes += f'- R$ {saque:.2f}\n'
		
def extrato():
	print(f'Operações realizadas hoje:\n{operacoes}\nSaldo atual da conta: R$ \n{saldo:.2f}')


while True:
	print('''		
Menu Principal
Aperte o número correspondente a operação desejada
[1]Deposito
[2]Saque
[3]Ver extrato
[4]Sair
	''')
	opcao = int(input())
	if opcao == 1:
		depositar()
	if opcao == 2:
		if contLim<3:
			sacar()
		else:
			print('Limite diario de saques atingido')
	if opcao == 3:
		extrato()
	if opcao == 4:
		break