#jogo da forca
palavra = 'Paulo Ito'
palavraFinal=''
palpite = ''
tentativas=[' ']#lista que terá todas as letras tentadas anteriormente, já vem com o espaço
forca=6
dica='Meu nome'
#está bem difente da versão anterior por causa de um codigo da internet
while True:
	tentativas =[' ']
	palavra = input('Digite a palavra para o outro jogador tentar descobrir\n')
	dica=input('Dica: ')
	forca = 6
	palavraFinal=''
	print('\n'*70)#tentativa de esconder a palavra que foi digitada
	while True:
		#irá criar uma palavra com todas as letras descobertas e colocará ._. no lugar das que estão faltando
		for letra in palavra:
			palavraFinal += letra if letra in tentativas else '._.'#isso fez diferença pra mim quando li um código de outra pessoa
		#condições para fim de jogo
		if palavraFinal == palavra:
			print('Você acertou!!!, a palavra é: {}!'.format(palavra))
			print('===================================================')
			break
		if forca == 0:
			print('Enforcado!!!, a palavra era: {}'.format(palavra))
			print('===================================================')
			break
		#mensagens para o usuário
		print('================ Jogo da forca ====================')
		print('Palavra:')
		print(palavraFinal)
		print('Chances restantes: {}'.format(forca))
		print('Dica:{}'.format(dica))
		palpite = input('Digite uma letra para tentar descobrir a palavra: ')

		#verifica se a palavra já foi escolhida, se tiver mais de uma ele avisa e não desconta na chance
		if palpite in tentativas:
			print('Você já tentou essa letra')
		elif len(palpite)>1:
			print('Só pode uma letra por vez')
		elif palpite.upper() not in palavra and palpite.lower() not in palavra:
			forca-=1#só desconta se for UMA letra errada, mais de uma é erro de digitação, não de escolha

		#tudo que foi digitado na variavel vai ficar na lista de tentativas
		tentativas.append(palpite.upper())#dessa forma não importa se tem letra maiuscula ou minuscula na palavra ou na escolha delas
		tentativas.append(palpite.lower())
		palavraFinal=''#é necessário resetar a variavel palavraFinal em no fim do loop
	#decisão para continuar no loop
	escolha = input('Aperte n pra sair ou qualquer tecla pra jogar outra vez: ')
	if escolha.lower() =='n':
		print('Fim de jogo, saindo do programa...')
		break		