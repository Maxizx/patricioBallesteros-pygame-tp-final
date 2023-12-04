import pygame as pg
import sys
from player import Player
from enemigo import Enemy
from niveles.plataforma import *
from botin import Frutas
from musica import audio
from auxiliar import Auxiliar
# from inicio import *

pg.font.init()
screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
fuente = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",30)
fuente_1 = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",29)
pg.init()
clock = pg.time.Clock()

imagen_fondo = Auxiliar.load_image_and_scale("images/locations/fondos/Purple.png",ANCHO_VENTANA,ALTO_VENTANA)
imagen_fondo2 = Auxiliar.load_image_and_scale("images/locations/fondos/Blue.png",ANCHO_VENTANA,ALTO_VENTANA)
vidas = Auxiliar.load_image_and_scale("images/corazo.png",50,50)


#llamado al escenario
player_1 = Player(config_player)
enemigo_1= Enemy(0, 0, 4, 8, 8, 16)
fruta_1 = Frutas(200,300)


musica_de_fondo = audio("musica_de_fondo",repetir=-1)

#camara_x = player_1.move_x
while True:

    relog = pg.time.get_ticks()//1000
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        # musica_de_fondo.play(-1)
        musica_de_fondo.reproducir_audio()
        lista_teclas_presionadas = pg.key.get_pressed()
        if lista_teclas_presionadas[pg.K_i]:
            # main_menu()
            print("sin vidas")
        if lista_teclas_presionadas[pg.K_UP]:
            musica_de_fondo.control_volumen(True)
            print(f"el volmen actual es de {musica_de_fondo.get_volumen_del_audio()}")
        if lista_teclas_presionadas[pg.K_DOWN]:
            musica_de_fondo.control_volumen(False)
            print(f"el volmen actual es de {musica_de_fondo.get_volumen_del_audio()}")
        

        player_1.selector_de_movimiento(lista_teclas_presionadas)
        enemigo_1.caminar_direccion(True)

    # camara_x = -player_1.rect[0] % imagen_fondo2.get_rect().width
    camara_x = -player_1.rect[0] % ANCHO_VENTANA
    #print(player_1.rect)
    
    #camara_x = -player_1.move_x
    screen.blit(imagen_fondo2, imagen_fondo2.get_rect(topleft=(player_1.movimiento_horizontal_de_la_camara(imagen_fondo2.get_rect().width),0)))
    if camara_x < ANCHO_VENTANA:
        screen.blit(imagen_fondo2,(camara_x,0))

    if player_1.lives == 0:
        # game_over()
        print("Game Over")
        pg.quit()
        sys.exit()

    for muro in muros:
        player_1.colision_con_objetos(muro)
        enemigo_1.colision_con_objetos(muro)

    fruta_1.colision_con_fruta(player_1)
    player_1.colision_con_enemigo(enemigo_1)

    
    dibujar_muros(screen,muros)
    enemigo_1.update()
    enemigo_1.draw(screen)
    player_1.update()
    player_1.draw(screen)
    fruta_1.update()
    fruta_1.draw(screen)

    contador = fuente_1.render(f"Time {str(relog)}",True,(255,255,255),(0,0,0))
    contador_vidas = fuente_1.render(str(player_1.lives),False,(0,0,0))
    screen.blit(vidas,(80,13))
    screen.blit(contador_vidas,(100,30))
    screen.blit(contador,(150,30))

    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pg.display.flip()

    delta_ms = clock.tick(FPS)

