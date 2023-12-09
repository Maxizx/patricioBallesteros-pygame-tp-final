
from botin import Frutas
from player import Player 
from enemigo import Enemy
from musica import audio
from constantes import *
from niveles.plataforma import (construir_mapas)
from auxiliar import Auxiliar
import random as rd




# class Game():
#     def __init__(self) -> None:
#         self.win = False
#         self.coordenadas_de_inicio = 0

#     def gano():
#         match "level":
#             case "level_1":
#                 pass
#             case "level_2":
#                 pass
#             case "level_3":
#                 pass

import pygame as pg
import sys
from player import Player


class GameManager(Frutas,pg.sprite.Sprite):
    def __init__(self, nivel=0):
        pg.font.init()
        pg.init()
        pg.display.set_caption("Island Adventure")
        self.screen_width = ANCHO_VENTANA
        self.screen_height = ALTO_VENTANA
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pg.time.Clock()
        self.frame_rate = FPS
        self.debug = False
        self.win = False
        self.win_level = False
        self.musica_de_fondo = audio("musica_de_fondo",repetir=-1)
        self.fuente = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",30)
        self.fuente_1 = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",29)   
        self.imagen_fondo = Auxiliar.load_image_and_scale("images/locations/fondos/Purple.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.imagen_fondo2 = Auxiliar.load_image_and_scale("images/locations/fondos/Blue.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.vidas = Auxiliar.load_image_and_scale("images/corazo.png",50,50)
        self.player_1 = Player(config_player)
        # self.enemigo_1= Enemy(0, 0, 4, 8, 8, 16)
        # self.fruta_1 = Frutas(200,300)
        self.fruta = Frutas()
        self.enemigo = Enemy(0,0)
        self.lista_de_niveles = lista_niveles
        self.nivel = nivel
        self.escenario =  0
        self.mapas = construir_mapas(0,0)
        self.fruta.spawn_frutas()
        self.enemigo.spawn_enemigos()
        self.cargar_mapa()




    def run(self):
        """
        Ejecuta el bucle principal del juego.
        """
        while True:
            relog = pg.time.get_ticks()//1000
            self.musica_de_fondo.reproducir_audio()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                lista_teclas_presionadas = pg.key.get_pressed()
                if lista_teclas_presionadas[pg.K_i]:
                    # main_menu()
                    print("sin vidas")
                if lista_teclas_presionadas[pg.K_UP]:
                    self.musica_de_fondo.control_volumen(True)
                    print(f"el volmen actual es de {self.musica_de_fondo.get_volumen_del_audio()}")
                if lista_teclas_presionadas[pg.K_DOWN]:
                    self.musica_de_fondo.control_volumen(False)
                    print(f"el volmen actual es de {self.musica_de_fondo.get_volumen_del_audio()}")
                
                self.player_1.selector_de_movimiento(lista_teclas_presionadas)
                self.enemigo.caminar_direccion(True)
                

            # camara_x = -self.player_1.rect[0] % self.imagen_fondo2.get_rect().width
            camara_x = -self.player_1.rect[0] % ANCHO_VENTANA
            #print(self.player_1.rect)
            
            #camara_x = -self.player_1.move_x
            self.screen.blit(self.imagen_fondo2, self.imagen_fondo2.get_rect(topleft=(self.player_1.movimiento_horizontal_de_la_camara(self.imagen_fondo2.get_rect().width),0)))
            if camara_x < ANCHO_VENTANA:
                self.screen.blit(self.imagen_fondo2,(camara_x,0))
                
            if self.player_1.lives == 0:
                self.gameover()

            self.colision_con_objetos_enemigo(self.enemigo.grupo_enemigos)
            self.colision_con_objetos(self.player_1)
            self.colision_con_objetos(self.enemigo)
            self.colision_con_fruta(self.player_1)
            self.colision_con_enemigo(self.player_1)
            
            self.enemigo.grupo_enemigos.update()
            self.enemigo
            self.enemigo.grupo_enemigos.draw(self.screen)
            self.player_1.update()
            self.player_1.draw(self.screen)
            self.fruta.grupo_frutas.draw(self.screen)
            self.fruta.grupo_frutas.update()
            self.mapas.grupo_bloques.draw(self.screen)
            self.mapas.grupo_bloques.update()


            contador = self.fuente_1.render(f"Time {str(relog)}",True,(255,255,255),(0,0,0))
            contador_vidas = self.fuente_1.render(str(self.player_1.lives),False,(0,0,0))
            contador_score_jugador = self.fuente_1.render(f"Score: {str(self.player_1.score)}",False,(255,255,255),(0,0,0) )
            nivel = self.fuente.render(f"NIVEL: {str(self.nivel + 1)}",False,(255,255,255),(0,0,0) )
            self.screen.blit(self.vidas,(80,13))
            self.screen.blit(contador_vidas,(100,30))
            self.screen.blit(contador,(150,30))
            self.screen.blit(contador_score_jugador,(ANCHO_VENTANA-300,30))
            self.screen.blit(nivel,(ANCHO_VENTANA/2,30))
            
            # enemigos update
            # player dibujarlo
            # dibujar todo el nivel


            pg.display.flip()


    def gameover(self):
        
            # game_over()
            print("Game Over")
            pg.quit()
            sys.exit()

    def eleccion_nivel(self, lista_de_niveles,nivel_elegido,escenario_elegido) -> str:
        for numero_de_nivel in range(len(lista_de_niveles)):
            if numero_de_nivel == nivel_elegido:
                nivel = f"level_{numero_de_nivel}"
                level = lista_de_niveles.get(nivel)

                for escenario in range(len(nivel)- 1):
                    if escenario == escenario_elegido:
                        # print(f"nivel : {nivel}, escenario: {escenario}")
                        escenario_a_cargar = level.get(f"{escenario}_escenario")
                        return escenario_a_cargar

    def cargar_mapa(self):
        self.mapa = self.eleccion_nivel(self.lista_de_niveles,self.nivel,self.escenario)
        self.muros = self.mapas.construir_mapa(self.mapa)


    def pasar_escenario(self):
        self.escenario += 1
        self.eleccion_nivel(self.lista_de_niveles,self.nivel,self.escenario)
        

    def colision_con_objetos(self,objeto):
        bloque_colisiona =  pg.sprite.spritecollideany(objeto,self.mapas.grupo_bloques)
        if bloque_colisiona:
        # if self.rect.colliderect(objeto):
            if objeto.rect[1] <= bloque_colisiona.rect.top :
                objeto.rect.bottom = bloque_colisiona.rect.top

            elif objeto.rect[1] < bloque_colisiona.rect.bottom and objeto.rect.bottom > bloque_colisiona.rect.bottom:
                objeto.rect.top = bloque_colisiona.rect.bottom
                # print(f"rectangulo Y:{objeto.rect[1]}, Bloque parte de abajo{bloque_colisiona.rect.bottom}")
                # print("choqué arriba")
            elif objeto.rect[0] < bloque_colisiona.rect.left:
                objeto.rect.right = bloque_colisiona.rect.left
                # print("choqué a la derecha")
            elif objeto.rect[0] <= bloque_colisiona.rect.right:
                objeto.rect.left = bloque_colisiona.rect.right
                # print("choqué a la izquiera")

    def colision_con_objetos_enemigo(self,grupo_de_sprites):
        for objeto in grupo_de_sprites:
            bloque_colisiona =  pg.sprite.spritecollideany(objeto,self.mapas.grupo_bloques)
            if bloque_colisiona:
            # if self.rect.colliderect(objeto):
                if objeto.rect[1] < bloque_colisiona.rect.top:
                    objeto.rect.bottom = bloque_colisiona.rect.top

                elif objeto.rect[0] < bloque_colisiona.rect.left:
                    objeto.rect.right = bloque_colisiona.rect.left
                    self.enemigo.caminar_direccion(True)

                elif objeto.rect[0] <= bloque_colisiona.rect.right:
                    objeto.rect.left = bloque_colisiona.rect.right
                    self.enemigo.caminar_direccion(False)


    def colision_con_fruta(self,objeto):
        if pg.sprite.spritecollide(objeto,group = self.fruta.grupo_frutas,dokill = True):
        # if self.rect.colliderect(objeto):
            print("frutaaa")
            self.player_1.score += self.fruta.puntos
            print(self.player_1.score)

    def colision_con_enemigo(self,objeto):
        if pg.sprite.spritecollide(objeto,self.enemigo.grupo_enemigos,dokill=False):
            # if self.rect.colliderect(objeto):
                if (pg.time.get_ticks() - self.enemigo.tiempo_entre_hits) > self.enemigo.cooldown_de_hit:
                    self.player_1.lives -=1
                    self.enemigo.tiempo_entre_hits = pg.time.get_ticks()
