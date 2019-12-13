import pygame
from pygame.locals import *
from imagem import Imagem

class Bala(Imagem):
    def __init__(self,src, posx, posy, vel):
        super().__init__(src, posx, posy)
        self.velocidadeBala=vel

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala
