def quickSortIterativo(array):
    #autor: ChatGPT
    # Validação da entrada
    if array == None or len(array) == 0:
        return
    
    # Use uma lista como uma pilha para evitar recursão
    stack = []
    stack.append(0)
    stack.append(len(array) - 1)
    
    while len(stack) > 0:
        # Obtenha os índices do topo da pilha
        fim = stack.pop()
        inicio = stack.pop()

        # Obtenha o índice divisor e divida a matriz em duas partes
        divisor = dividir(array, inicio, fim)

        # Adicione os índices das partes menores e maiores à pilha
        if divisor - 1 > inicio:
            stack.append(inicio)
            stack.append(divisor - 1)
        
        if divisor + 1 < fim:
            stack.append(divisor + 1)
            stack.append(fim)
def dividir(lista, inicio, fim):
    # Use o valor médio como pivô
    meio = (inicio + fim) // 2
    pivot = lista[meio]

    # Coloque o pivô no final da lista
    lista[meio], lista[fim] = lista[fim], lista[meio]

    index_pivot = inicio
    for i in range(inicio, fim):
        if lista[i] <= pivot:
            lista[i], lista[index_pivot] = lista[index_pivot], lista[i]
            index_pivot += 1

    # Coloque o pivô em seu lugar correto
    lista[index_pivot], lista[fim] = lista[fim], lista[index_pivot]

    return index_pivot
lista = [5,4,2,1,3]
quickSortIterativo(lista)
print(lista)