import pygame
from pygame.locals import *
from bala import Bala
from personagem import Personagem
from imagem import Imagem


# classe nave do jogador
class Nave(Personagem):
    __listaDisparo = []

    def __init__(self, src, posx, posy, vel):
        super().__init__(src, posx, posy, vel)
        self.listaDisparo = []


    def disparar(self, x, y):
        self.minhaBala = Bala("imagens/tiro_nave.png", x, y, 5)
        self.listaDisparo.append(self.minhaBala)


    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0

        elif self.rect.right >= 900:
            self.rect.right = 900
