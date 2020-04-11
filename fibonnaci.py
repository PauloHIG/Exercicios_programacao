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

print(fiboSolução(40))

#abaixo está a solução que eu copiei de um artigo da internet
def f(n):
	raiz5 = sqrt(5)
	return int((1/raiz5)*(pow((1+raiz5)/2,n)-pow((1-raiz5)/2,n)))

for i in range(42):
	print(f(i))