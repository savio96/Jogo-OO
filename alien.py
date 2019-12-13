import pygame
from pygame.locals import *
from personagem import Personagem
from imagem import Imagem

class Alien(Personagem):
    def __init__(self,src, posx, posy, vel):
        super().__init__(src, posx, posy, vel)

    def movimento(self):
        self.rect.left = self.rect.left + self.velocidade
        if self.rect.left >= 850:
            self.velocidade *= -1
            self.rect.top = self.rect.top + 50
        if self.rect.left <= 0:
            self.velocidade *= -1
            self.rect.top = self.rect.top + 50