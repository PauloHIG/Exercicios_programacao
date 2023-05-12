# https://adventofcode.com/2022/day/3
with open("inputs_desafios/day_3.txt") as input_desafio:
    rucksacks = input_desafio.read()
def procuraItemComum(metade1,metade2):
    """Retorna o valor do peso da letra em comum entre as duas metades do texto de acordo com o desafio"""
    for letra in metade1:
        if letra in metade2:
            if letra.islower():
                return  ord(letra)-96
            if letra.isupper():
                return  ord(letra)-38
    return 0

sacos = rucksacks.split('\n')
# parte 1
soma = 0
for saco in sacos:
    metade1 = saco[:len(saco)//2]
    metade2 = saco[len(saco)//2:]
    soma+= procuraItemComum(metade1,metade2)
print(soma)

# parte 2 
sacos = rucksacks.split('\n')
soma = 0
#irei incrementar de 3 em 3 
incremento = 0
for i in range(len(sacos)//3):
    # o set me permite saber a diferença entre conjuntos de modo simples
    item_comum = (set(sacos[0+incremento]) & set(sacos[1+incremento]) & set(sacos[2+incremento])).pop()
    if item_comum.isupper():
        soma+=ord(item_comum)-38
    if item_comum.islower():
        soma+=ord(item_comum)-96
    incremento+=3
print(soma)
