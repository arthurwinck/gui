from pygame.sprite import Sprite
#Será que precisa importar pygame inteiro?
import pygame as py

class TelaMesa(Sprite):
    #TODO - ATUALIZAR DIAGRAMA PARA PARAMETRO DISPLAY
    #TODO - ATUALIZAR DIAGRAMA PARA RETIRAR RECT?
    def __init__(self, display):
        super().__init__()
        self.superficie = display.set_mode((1280,720))
        self.telaX, self.telaY = py.display.get_surface().get_size()
        self.tamX = 1000
        self.tamY = 500
        #calculo para descobrir os pontos x e y para iniciar o desenho da mesa
        #x e y inicial e largura e altura
        self.tamPos = ((self.telaX - self.tamX)/2,(self.telaY - self.tamY)/2, self.tamX, self.tamY)
        #variável que teria que ser colocada em um arquivo de configuração
        self.green = (34, 161, 65)

    def desenharMesa(self):
        self.superficie.fill((82,91,247))
        py.draw.rect(self.superficie, self.green, self.tamPos)
        
        for i in range(3):
            for j in range(2):
                py.draw.circle(self.superficie, self.green, ((self.telaX - self.tamX)/2 + (self.tamX/2)*i, (self.telaY - self.tamY)/2 + (self.tamY)*j), 25)

    def desenharBolas(self, bolas):
        for bola in bolas:
            pos_x, pos_y = bola.getPosicao()
            vel_x, vel_y = bola.getVelocidade()
            
            py.draw.circle(self.superficie, bola.cor, (pos_x,pos_y), 15)   