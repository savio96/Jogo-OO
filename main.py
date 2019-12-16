import sys
import os
import time
import pygame
from pygame.locals import *
from imagem import Imagem
from alien import Alien
from nave import Nave


def spaceWars():
    pygame.init()
    dimensao = (900, 700)
    tela = pygame.display.set_mode(dimensao)
    pygame.display.set_caption("Space Wars")
    relogio = pygame.time.Clock()
    tempo = 0
    listaInimigo = []  # criar lista de inimigos
    posxAlien = 10  # posição no eixo x inicial dos aliens
    posyAlien = 50  # posição no eixo y inicial dos aliens
    for ini in range(10):  # loop para colocar os aliens em uma lista com posiçôes diferentes
        posxAlien += 80
        inimigo = Alien("imagens/alien.png", posxAlien, posyAlien, 10)
        listaInimigo.append(inimigo)
    inimigos = listaInimigo
    jogando = False  # status jogo
    menu = True  # status jogo
    fundo = Imagem("imagens/menu.jpg", 0, 0)  # imagens que aparecem no jogo
    fundoPlay = Imagem("imagens/fundo.jpg", 0, 0)
    jogar = Imagem("imagens/play.png", 350, 100)
    sair = Imagem("imagens/exit.png", 350, 300)
    win = Imagem("imagens/win.png", 270, 240)
    lose = Imagem("imagens/lose.png", 350, 100)
    restart = Imagem("imagens/restart.png", 280, 400)
    jogador = Nave("imagens/nave.png", 450, 650, 20)

    while True:
        if menu == True:
            for evento in pygame.event.get():  # loop para pegar evento do mouse do jogo
                if evento.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed() and jogar.rect.collidepoint(
                            pygame.mouse.get_pos()):
                        jogando = True
                        menu = False
                    if pygame.mouse.get_pressed() and sair.rect.collidepoint(
                            pygame.mouse.get_pos()):
                        pygame.quit()  # sair jogo
                        sys.exit()  # sair sistema

            fundo.colocar(tela)
            jogar.colocar(tela)
            sair.colocar(tela)
        if jogando == True:
            fundoPlay.colocar(tela)
            jogador.colocar(tela)
            relogio.tick(60)  # fps do jogo
            tempo = int(pygame.time.get_ticks() / 1000)  # pegar o tempo do jogo
            for evento in pygame.event.get():  # loop para pegar evento do teclado do jogo
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:  # movimento jogador esquerda
                        jogador.movimentoEsquerda()
                    elif evento.key == K_RIGHT:  # movimento jogador direita
                        jogador.movimentoDireita()
                    elif evento.key == K_SPACE:  # disparar tiro jogador
                        x, y = jogador.rect.center  # coordenadas de onde sai o tiro
                        jogador.disparar(x, y)
                    elif evento.key == K_KP_ENTER or K_TAB:
                        menu = True
                        jogando = False
                        spaceWars()  # reinicia o jogo
            if len(jogador.listaDisparo) > 0:  # movimento bala na tela
                for x in jogador.listaDisparo:
                    x.colocar(tela)  # colocar as balas na tela que estão dentro da lista
                    x.trajetoria()  # movimento bala
                    if x.rect.top < -10:
                        jogador.listaDisparo.remove(x)  # remove bala da lista quando ela sai da tela
            if len(listaInimigo) > 0:  # confere para ver se o jogo ainda está rodando
                for x in listaInimigo:
                    x.colocar(tela)  # desenha os inimigos na tela
                    x.movimento()  # movimenta os inimigos
                    for z in jogador.listaDisparo:
                        if pygame.sprite.collide_rect(x, z) and x.vida == True:  # verifica a colisão da bala e inimigo
                            x.vida = False
                            listaInimigo.remove(x)  # remove o inimigo atingido
                            jogador.listaDisparo.remove(z)  # remove a bala
                    if x.rect.top >= 650:  # verifica a derrota do jogador
                        jogador.vida = False
                        lose.colocar(tela)
                        restart.colocar(tela)
            if len(listaInimigo) == 0:
                win.colocar(tela)
                restart.colocar(tela)
        pygame.display.update()


spaceWars()
