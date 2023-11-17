import pygame as pg
import sys
from constantes import *
from player import Player
from enemigo import Enemy
import random
import auxiliar


screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()


imagen_fondo = pg.image.load("images/locations/fondos/Purple.png")
imagen_fondo = pg.transform.scale(imagen_fondo, (ANCHO_VENTANA + 1000, ALTO_VENTANA))
imagen_fondo = pg.image.load("images/locations/fondos/Blue.png")
imagen_fondo2 = pg.transform.scale(imagen_fondo, (ANCHO_VENTANA + 1000, ALTO_VENTANA))


player_1 = Player(0, 0, 4, 8, 8, 16)
enemigo_1= Enemy(ANCHO_VENTANA, 0, 4, 8, 8, 16)

fondo_actual = imagen_fondo
camara_x = player_1.move_x
primera = True
player_rect = (200, 500, 50, 50)


while True:
    relog = pg.time.get_ticks()/1000
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        lista_teclas_presionadas = pg.key.get_pressed()
        # if event.type == pg.KEYDOWN:
        if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
            player_1.control("WALK_L")
        if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
            player_1.control("WALK_R")
        if lista_teclas_presionadas[pg.K_SPACE]:
            player_1.control("JUMP_R")
        if lista_teclas_presionadas[pg.K_SPACE] and lista_teclas_presionadas[pg.K_LEFT]:
            player_1.control("JUMP_L")
        if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
            player_1.control("STAY")

    camara_x = -player_1.rect[0] % imagen_fondo2.get_rect().width

    print(player_1.rect)

    #camara_x = -player_1.move_x
    screen.blit(imagen_fondo2, imagen_fondo2.get_rect(topleft=(camara_x - imagen_fondo2.get_rect().width,0)))
    if camara_x < ANCHO_VENTANA:
        screen.blit(imagen_fondo2,(camara_x,0))

    rectangulo = pg.draw.rect(screen, (0,   255,   0),player_rect)
    circulo = pg.draw.circle(screen,(0,0,0), (100,500),radius=20)

    if player_1.rect.colliderect(rectangulo):
        player_1.rect[0] -=  player_1.move_x 


    enemigo_1.update()
    enemigo_1.draw(screen)
    player_1.update()
    player_1.draw(screen)

    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pg.display.flip()

    delta_ms = clock.tick(FPS)
