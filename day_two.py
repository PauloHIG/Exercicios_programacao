with open("day_two.txt") as input_do_desafio:
    partidas = input_do_desafio.read()

#https://adventofcode.com/2022/day/2/answer
#A pedra B papel C tesoura | X Perder Y Empatar Z Vencer
valores_empate = {"A":4,"B":5,"C":6}
valores_vitoria = {"A":8,"B":9,"C":7}
valores_derrota = {"A":3,"B":1,"C":2}

pontuação = 0
partidas = partidas.split('\n')
for partida in partidas:
    if partida[2] == "X":
        pontuação+=valores_derrota[partida[0]]
    if partida[2] == "Y":
        pontuação+=valores_empate[partida[0]]
    if partida[2] == "Z":
        pontuação+=valores_vitoria[partida[0]]
print(pontuação)