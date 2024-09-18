# Apenas um código teste

import pygame
import time
import random

pygame.init()

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

largura_tela = 600
altura_tela = 400

tamanho_bloco = 10
velocidade = 15

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

def exibir_placar(score):
    fonte = pygame.font.SysFont(None, 35)
    texto = fonte.render("Pontos: " + str(score), True, preto)
    tela.blit(texto, [0, 0])

def jogo():
    fim_de_jogo = False
    fechar_jogo = False

    x = largura_tela / 2
    y = altura_tela / 2

    x_mudar = 0
    y_mudar = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0

    relogio = pygame.time.Clock()

    while not fim_de_jogo:

        while fechar_jogo:
            tela.fill(branco)
            fonte_fim = pygame.font.SysFont(None, 50)
            mensagem = fonte_fim.render("Fim de Jogo! Pressione C para jogar de novo ou Q para sair", True, vermelho)
            tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
            exibir_placar(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_de_jogo = True
                        fechar_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudar = -tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudar = tamanho_bloco
                    y_mudar = 0
                elif evento.key == pygame.K_UP:
                    y_mudar = -tamanho_bloco
                    x_mudar = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudar = tamanho_bloco
                    x_mudar = 0

        if x >= largura_tela or x < 0 or y >= altura_tela or y < 0:
            fechar_jogo = True

        x += x_mudar
        y += y_mudar
        tela.fill(branco)

        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        corpo_cobra.append(cabeca_cobra)

        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca_cobra:
                fechar_jogo = True

        for segmento in corpo_cobra:
            pygame.draw.rect(tela, preto, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        exibir_placar(comprimento_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()

