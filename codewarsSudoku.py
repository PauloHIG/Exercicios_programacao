import numpy as np
def done_or_not(aboard): #board[i][j]
  #com esse código, devo aprender como se usa colunas e linhas em python
  board = np.array(aboard)#uma lista de lista é transformada em uma array
  rows = [board[i,:] for i in range(9)]#linhas, a vírgula só é usada em arrays
  cols = [board[:,j] for j in range(9)]#colunas
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]#quadrados de 3x3
  #o flatten "achata" o array para uma dimensão
  for view in np.vstack((rows,cols,sqrs)):#mostra matrizes em sequência, só funciona com matrizes, por isso foi necessário um flatte() no array dos quadrados
      if len(np.unique(view)) != 9:#procura elementos únicos no array, conheçendo as regras do sudoku, não é difícil entender que a lista precisa ter exatamente 9 elementos
          return 'Try again!'#caso o tamanho do array seja menor que 9, é porque um ou mais dos elementos não foram 'únicos' ex:[1,1,2] vira [1,2]
  
  return 'Finished!'
