#Contexto https://adventofcode.com/2022/day/1
materia_bruta = 0 #https://adventofcode.com/2022/day/1/input o input do desafio está aqui, uma lista enorme de números
materia_bruta = materia_bruta.split(' ')
materia_bruta = materia_bruta[0].split('\n\n')
joia_lapidada =[]
for materia in materia_bruta:
    joia_lapidada.append(materia.split('\n')) 
joia_polida = []
for joia in joia_lapidada:
    joia_polida.append(list(map(int,joia)))
lista_somas = list(map(sum,joia_polida))
soma = 0
for i in range(3):
    soma+=max(lista_somas)
    lista_somas.remove(max(lista_somas))
print(soma)