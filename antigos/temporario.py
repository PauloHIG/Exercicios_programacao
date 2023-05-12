def função(a, b):
	return a+b
def recebeFunção(fun):
	print(fun)
	return fun == 7
print(recebeFunção(função(2,5)))