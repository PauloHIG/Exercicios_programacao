#Ping pong em Python
#esse foi copiado de um tutorial do Youtube
import pygame
from pygame.locals import *
from OpenGL.GL import *

largura_janela = 640
altura_janela = 480

#variaveis da posiçao, tamanho e velocidade da bola
xBola = 0
yBola = 0
tamBola = 20
VelBolax = 3
VelBolay = 3
#posiçao das "Raquetes"
yJogador1 = 0
yJogador2 = 0

def xDojogador1():
	return -largura_janela / 2 + larguraDosJogadores()/2
def xDojogador2():
	return largura_janela / 2 - larguraDosJogadores()/2
def larguraDosJogadores():
	return 20
def alturaDosJogadores():
	return 3 * 20	

def atualizar():
	global xBola, yBola, VelBolax, VelBolay, yJogador1, yJogador2,tamBola
	xBola = xBola + VelBolax
	yBola = yBola + VelBolay
	if (xBola + tamBola / 2 > xDojogador2() - larguraDosJogadores() / 2 
		and yBola - tamBola / 2 < yJogador2 + alturaDosJogadores() / 2 
		and yBola + tamBola / 2 > yJogador2 - alturaDosJogadores() / 2):
		VelBolax = -VelBolax

	if (xBola - tamBola / 2 < xDojogador1() + larguraDosJogadores() / 2 
		and yBola - tamBola / 2 < yJogador1 + alturaDosJogadores() / 2 
		and yBola + tamBola / 2 > yJogador1 - alturaDosJogadores() / 2):
		VelBolax = -VelBolax

	if yBola + tamBola / 2 > altura_janela / 2:
		VelBolay = -VelBolay 
	if yBola - tamBola / 2 < -altura_janela / 2:
		VelBolay = -VelBolay
	if xBola < -largura_janela / 2 or xBola > largura_janela / 2:
		xBola = 0
		yBola = 0
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		yJogador1 = yJogador1 + 5
	if keys[K_s]:
		yJogador1 = yJogador1 - 5
	if keys[K_UP]:
		yJogador2 = yJogador2 + 5
	if keys[K_DOWN]:
		yJogador2 = yJogador2 - 5
	if tamBola == 0:
		system.exit()


def desenharRetangulo(x,y,largura,altura,r,g,b):
	glColor3f(r,g,b)
	glBegin(GL_QUADS)
	glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
	glVertex2f(0.5 * largura + x, -0.5 * altura + y)
	glVertex2f(0.5 * largura + x, 0.5 * altura + y)
	glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
	glEnd()

def desenhar():	
	glViewport(0,0,largura_janela,altura_janela)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-largura_janela/2, largura_janela/2, -altura_janela/2, altura_janela/2,0,1)
	glClear(GL_COLOR_BUFFER_BIT)
	desenharRetangulo(xBola,yBola,tamBola,tamBola,1,1,0)
	desenharRetangulo(xDojogador1(),yJogador1,larguraDosJogadores(),alturaDosJogadores(),1,0,0)
	desenharRetangulo(xDojogador2(),yJogador2,larguraDosJogadores(),alturaDosJogadores(),0,0,1)
	pygame.display.flip()


#criaçao de uma janela com o pygame
pygame.init()
pygame.display.set_mode((largura_janela,altura_janela), DOUBLEBUF|OPENGL)

#gameloop, para a janela não fechar logo ao abrir
while True:
	desenhar()
	atualizar()
	pygame.event.pump()
	#esse código é para o botão de fechar da janela funcionar
	for event in pygame.event.get():
	 	if event.type == pygame.QUIT:
	 		pygame.quit()
	 		exit()
            
                
                
