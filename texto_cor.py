from colorama import init
#o termcolor é outro módulo de cor, mas funciona junto com o colorama se eu usar o init()
from termcolor import colored

#o colorama só funciona no windows se eu usar o init()
init()
#função pra criar cor vermelha usando o ANSI
def vermelho(skk):print("\u001b[31;1m {}\033[00m".format(skk))
vermelho("Olá mundo")

#print com o colored do termcolor, o meu terminal só suporta 8 cores
print(colored('Vou dominar o mundo','green'))
'''
as cores que posso usar no colored()
grey
red
green
yellow
blue
magenta
cyan
white'''