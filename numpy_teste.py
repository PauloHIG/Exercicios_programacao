#numpy para trabalhar com matrizes

#exemplo pego de um tutorial na internet
#sempre importe o numpy como np, é uma convenção
import numpy as np

# Make the array `my_array`
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

# Print `my_array`
print(my_array)

ArrayBatata = np.full((4,4),"Batata")
print(ArrayBatata)

arrayLivre = np.empty((5,5))
print(arrayLivre)