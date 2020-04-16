#jogo da forca
palavra = 'Hello world'
palavraFinal=''
letra = ' '
palavraVazia=[]#lista pra poder recever cada letra acertada da palavra digitada
tentativas=[]#lista que terá todas as letras tentadas anteriormente
forca=3

#para que a lista tenha sempre o mesmo tamanho da palavra digitada
for i in range(len(palavra)):
	palavraVazia.append(' ')

def verificar(tentativas:list):
	while True:
		letra=input('Digite uma letra: ')
		if letra.upper() in tentativas or letra.lower() in tentativas:
			print('você já tentou essa letra antes')
		elif len(letra)>1:
			print('só uma letra')
		else:
			tentativas.append(letra)
			return letra
			break
def substituir(letra,palavraVazia:list,palavra,chance:int):
	verchance=False
	for i in range(len(palavra)):
		if palavra[i] == letra.lower():
			palavraVazia[i] = letra.lower()
			verchance=True
		elif palavra[i] == letra.upper():
			palavraVazia[i]=letra.upper()
			verchance=True
	if verchance == False:
		chance-=1
		return chance
	else:
		return chance
def palavraCheia(palavraVazia:list,palavraFinal,palavra):
	for letra in palavraVazia:
		palavraFinal = palavraFinal+letra
	if palavraFinal == palavra:
		return False
	palavraFinal = ''

while True:
	letra = verificar(tentativas)
	forca = substituir(letra,palavraVazia,palavra,forca)
	print('chances:{}'.format(forca))
	print(palavraVazia)
	cont = palavraCheia(palavraVazia,palavraFinal,palavra)
	if cont== False:
		print('Parabens, a palavra era: {}'.format(palavra))
		break
	elif forca == 0:
		print('Enforcado!!, fim de jogo')
		break