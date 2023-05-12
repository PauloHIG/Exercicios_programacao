#fibonnaci
#este aqui fui eu que fiz
from math import sqrt,pow
def fiboSolução(n):
	fibo=[]
	n1=0
	n2=1
	fibo.append(n1)
	fibo.append(n2)
	for i in range(n):
		nf=n1+n2
		fibo.append(nf)
		n1=n2
		n2=nf
	return fibo
#aqui eu não pego o número de fibonnaci em uma posição específica, pego do 0 até o número que estiver na chamada da função
print(fiboSolução(40))

#abaixo está a solução que eu copiei de um artigo da internet, ela usa uma fórmula e calcula o número de acordo com a posição dele
def f(n):
	raiz5 = sqrt(5)
	return int((1/raiz5)*(pow((1+raiz5)/2,n)-pow((1-raiz5)/2,n)))
#se eu quiser saber em sequência os números de fibonnaci, eu preciso criar um for e chamar a função
for i in range(42):
	print(f(i))