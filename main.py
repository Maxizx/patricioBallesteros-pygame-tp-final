import pygame as pg
import sys
from constantes import *
from player import Player
from enemigo import Enemy
from niveles.plataforma import *
from botin import Frutas
from inicio import *


def game():
    screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    fuente = pg.font.SysFont("Arial",30)
    fuente_1 = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",29)

    pg.init()
    clock = pg.time.Clock()

    bloque_de_abajo = bloque()
    imagen_fondo = pg.image.load("images/locations/fondos/Purple.png")
    imagen_fondo = pg.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    imagen_fondo = pg.image.load("images/locations/fondos/Blue.png")
    imagen_fondo2 = pg.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    vidas = pg.image.load("images/corazo.png")
    vidas = pg.transform.scale(vidas, (50, 50))


    #llamado al escenario
    player_1 = Player(0, 0, 4, 8, 8, 16)
    enemigo_1= Enemy(0, 0, 4, 8, 8, 16)
    fruta_1 = Frutas(200,300)

    musica_de_fondo = pg.mixer.Sound("audio/musica_de_fondo.mp3")
    musica_de_fondo.set_volume(0.01)


    fondo_actual = imagen_fondo
    #camara_x = player_1.move_x
    primera = True
    player_rect = (200, 500, ANCHO_VENTANA, 50)

    while True:


        relog = pg.time.get_ticks()//1000
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            musica_de_fondo.play(-1)
            lista_teclas_presionadas = pg.key.get_pressed()
            if lista_teclas_presionadas[pg.K_i]:
                main_menu()

            player_1.selector_de_movimiento(lista_teclas_presionadas)

        # camara_x = -player_1.rect[0] % imagen_fondo2.get_rect().width
        camara_x = -player_1.rect[0] % ANCHO_VENTANA
        #print(player_1.rect)
        
        #camara_x = -player_1.move_x
        screen.blit(imagen_fondo2, imagen_fondo2.get_rect(topleft=(player_1.movimiento_horizontal_de_la_camara(imagen_fondo2.get_rect().width),0)))
        if camara_x < ANCHO_VENTANA:
            screen.blit(imagen_fondo2,(camara_x,0))

        if player_1.lives == 0:
            game_over()

        for muro in muros:
            player_1.colision_con_objetos(muro)
            enemigo_1.colision_con_objetos(muro)

        fruta_1.colision_con_fruta(player_1)

        
        dibujar_muros(screen,muros)
        bloque_de_abajo.draw_bloque(screen)
        enemigo_1.update()
        enemigo_1.draw(screen)
        player_1.update()
        player_1.draw(screen)
        fruta_1.update()
        fruta_1.draw(screen)

        contador = fuente_1.render(f"Time {str(relog)}",True,(255,255,255),(0,0,0))
        # vidas = fuente_1.render(f" vidas x{str(player_1.lives)}",False,(0,0,0),(255,255,255))
        contador_vidas = fuente_1.render(str(player_1.lives),False,(0,0,0))
        screen.blit(vidas,(80,13))
        screen.blit(contador_vidas,(100,30))
        screen.blit(contador,(150,30))




        # enemigos update
        # player dibujarlo
        # dibujar todo el nivel

        pg.display.flip()

        delta_ms = clock.tick(FPS)
