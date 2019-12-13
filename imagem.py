import pygame
from pygame.locals import *

class Imagem:
    __src = ""
    __rect = None
    __imagemRender = None

    def __init__(self, src, posx, posy):
        self.src = src
        self.ImagemRender = pygame.image.load(src)
        self.rect = self.ImagemRender.get_rect()
        self.rect.top = posy
        self.rect.left = posx


    def colocar(self, superficie):
        superficie.blit(self.ImagemRender, self.rect)

