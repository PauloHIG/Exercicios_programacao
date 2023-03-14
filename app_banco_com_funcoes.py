#cadastros pré preenchidos para economia de tempo
clientes = [
{'Nome': 'Paulo H. Ito', 'Nasc': '15/09/1998', 'CPF': 123123123, 'End': 'av maça 321, cidade depois da ponte, São Paulo, SP'},
{'Nome': 'Gregor', 'Nasc': '03/03/1997', 'CPF': 33341231220, 'End': 'av apple 123, gravity falls. huge city CA'}]
contas = [
{'agencia': '0001', 'conta': 1, 'tipo_conta': 'Corrente', 'CPF_usuario': 123123123, 'saldo': 0.0, 'limite_saque': 3, 'limite_qtd_saque': 500.0}, 
{'agencia': '0001', 'conta': 2, 'tipo_conta': 'Corrente', 'CPF_usuario': 123123123, 'saldo': 0.0, 'limite_saque': 3, 'limite_qtd_saque': 500.0}, 
{'agencia': '0001', 'conta': 3, 'tipo_conta': 'Corrente', 'CPF_usuario': 33341231220, 'saldo': 0.0, 'limite_saque': 3, 'limite_qtd_saque': 500.0}]

def recebe_cpf():
	while True:
		try:
			CPF = int(input('Digite o CPF, apenas os números: '))
		except ValueError:
			print('Não há necessidade de colocar o "-" antes do dígito')
			continue
		return CPF
def verifica_cpf(clientes,cpf):
	for cliente in clientes:
		if cpf == cliente['CPF']:
			#confirma se o cpf já está cadastrado no sistema
			return True
	return False
def cadastra_cliente(clientes):
	dic = {'Nome':'','Nasc':'','CPF':0,'End':''}
	cpf = recebe_cpf()
	if verifica_cpf(clientes,cpf):
		print('Já existe um usuario cadastrado com esse CPF')
		return 
	dic['Nome'] = input('Digite seu nome: ')
	dic['CPF'] = cpf
	dic['Nasc'] = input('Digite sua data de nascimento dia/mês/ano: ')
	dic['End'] = input('Digite o endereço Logradouro, Bairro, Cidade, sigla do estado: ')
	clientes.append(dic)
	print('Cliente cadastrado com sucesso')
def cria_conta(contas):
	cpf = int(input('Digite seu CPF para criar a conta: '))
	if verifica_cpf(clientes,cpf):
		conta_increment = len(contas)+1
		dic = {'agencia':'0001','conta':conta_increment,'tipo_conta':'Corrente','CPF_usuario':cpf,'saldo':0.00,'limite_saque':3,'limite_qtd_saque':500.00}
		contas.append(dic)
		print('conta criada com sucesso')
	else:
		print('Não podemos criar uma conta para um usuario não cadastrado em nosso sitema')
		return
def consulta_contas(contas):
	cpf = int(input('Digite seu CPF para ver suas contas: '))
	for conta in contas:
		if conta['CPF_usuario']==cpf:
			print(f"Agência {conta['agencia']} \nConta: {conta['conta']} \nCPF:{conta['CPF_usuario']}\n")
def seleciona_conta():
	consulta_contas(contas)
	num = int(input('Digite o numero da conta que quer usar: '))
	for conta in contas:
		if num == conta['conta']:
			return conta
def recebeNumero(texto='numero: '):
	while True:
		try:
			dinheiro = float(input(texto))
		except ValueError:
			print('Somente Valores numericos, e use ponto "." no lugar da vírgula "," ')
			continue
		if dinheiro<0.01:
			print('O limite mínimo de para qualquer operação no banco é de R$ 0.01')
			continue
		break
	return dinheiro
def depositar(saldo,operacoes,/):
	deposito = recebeNumero('Digite o valor que quer depositar: ')
	saldo = saldo+deposito
	print('Deposito realizado com sucesso')
	#informações para o extrato
	operacoes += f'+ R$ {deposito:.2f}\n'
	return saldo,operacoes
def sacar(*,saldo,operacoes,contLim,lim):
	if contLim==lim:
		print('você já atingiu o limite diario de saques')
		return saldo, operacoes, contLim
	saque = recebeNumero('Digite o valor que quer sacar: ')
	if saque>saldo:
		print('!!!!!Você não possui essa quantia para sacar!!!!')
	elif saque>500:
		print('!!!!!O limite é de R$ 500.00 por saque!!!!')
	else:
		saldo = saldo-saque
		contLim+=1
		print('Saque realizado com sucesso')
		#informações para o extrato
		operacoes += f'- R$ {saque:.2f}\n'
	return saldo, operacoes, contLim	
def extrato(saldo,/,*,operacoes):
	print(f'Operações realizadas hoje:\n{operacoes}\nSaldo atual da conta: \nR$ {saldo:.2f}')
#Funções de menus
def menu_principal():
	while True:
		print('''	
============================Menu Principal============================
	Aperte o número correspondente a operação desejada
	[1]Cadastrar usuario
	[2]Criar conta
	[3]Consultar contas
	[4]Sair''')
		opcao = int(input('_'))
		if opcao == 1:
			cadastra_cliente(clientes)
		if opcao == 2:
			cria_conta(contas)
		if opcao == 3:
			conta = seleciona_conta()
			operacoes_conta(conta)
		if opcao == 4:
			break

def operacoes_conta(conta):
	operacoes = ''
	contLim = 0
	while True:
		print('''	
============================Menu Principal============================
	Aperte o número correspondente a operação desejada
	[1]Deposito
	[2]Saque
	[3]Ver extrato
	[4]Sair ''')
		opcao = int(input('_'))
		if opcao == 1:
			conta['saldo'],operacoes = depositar(conta['saldo'],operacoes)
		if opcao == 2:
			conta['saldo'],operacoes,contLim= sacar(saldo=conta['saldo'],operacoes=operacoes,contLim=contLim,lim=conta['limite_saque'])
		if opcao == 3:
			extrato(conta['saldo'],operacoes=operacoes)
		if opcao == 4:
			break
menu_principal()