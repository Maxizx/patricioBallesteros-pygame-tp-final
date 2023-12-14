
from auxiliar.objetos.botin import Frutas
from auxiliar.objetos.player import Player 
from auxiliar.objetos.enemigo import Enemy
from auxiliar.musica import Audio
from auxiliar.constantes import *
from niveles.plataforma import (sierra,construir_mapas)
from auxiliar.auxiliar import Auxiliar
from interfaz.GUI_menus import menu
import pygame as pg
import sys
from auxiliar.objetos.player import Player


class GameManager(pg.sprite.Sprite):
    def __init__(self, nivel=0,escenario=0,score=0):
        pg.font.init()
        pg.init()
        pg.display.set_caption("Island Adventure")
        self.screen_width = ANCHO_VENTANA
        self.screen_height = ALTO_VENTANA
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pg.time.Clock()
        self.win = None
        self.frame_rate = 60
        self.valor_musica = 0
        self.debug = False
        self.ruido_recompensa = Audio("apple",volumen=1)
        self.musica_de_fondo = Audio("musica_de_fondo",repetir=-1)
        self.ruido_disparo = Audio("pop")
        self.fuente = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",30)
        self.fuente_1 = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",29)   
        self.imagen_fondo = Auxiliar.load_image_and_scale("images/locations/fondos/Purple.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.imagen_fondo2 = Auxiliar.load_image_and_scale("images/locations/fondos/Blue.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.vidas = Auxiliar.load_image_and_scale("images/corazo.png",50,50)
        self.player_1 = Player(config_player,score)
        self.fruta = Frutas()
        self.enemigo = Enemy()
        self.menu_ = menu()
        self.trampa = sierra()
        self.lista_de_niveles = lista_niveles
        self.nivel = nivel
        self.escenario =  escenario
        self.escenario_actual = self.escenario 
        self.tiempo_inicio = pg.time.get_ticks() 
        self.relog = 0
        self.mapas = construir_mapas()
        self.fruta.spawn_frutas(8)
        self.cargar_mapa()




    def run(self):
        """
        Ejecuta el bucle principal del juego.
        """
        self.musica_de_fondo.reproducir_audio()
        while True:
            self.clock.tick(self.frame_rate)
            self.relog = (pg.time.get_ticks() - self.tiempo_inicio) //1000 

            self.cambio_de_escenario()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                lista_teclas_presionadas = pg.key.get_pressed()
                if lista_teclas_presionadas[pg.K_i]:

                    self.valor_musica=self.menu_.pause()

                if lista_teclas_presionadas[pg.K_p]:
                        self.debug = True
                if lista_teclas_presionadas[pg.K_o]:
                        self.debug = False
                
                self.player_1.selector_de_movimiento(lista_teclas_presionadas)
                self.enemigo.caminar_direccion(True)
            
            self.screen.blit(self.imagen_fondo2, self.imagen_fondo2.get_rect(topleft=(0,0)))

            self.pantalla_final()

            self.volumen_modificar()

            self.colision_con_objetos_enemigo(self.enemigo.grupo_enemigos)
            self.colision_con_objetos(self.player_1)
            self.colision_con_objetos(self.enemigo)
            self.colision_con_fruta(self.player_1)
            self.colision_con_enemigo(self.player_1)
            self.colision_fruta_con_bloque(self.fruta.grupo_frutas)
            self.colision_con_trampa(self.player_1)


            self.enemigo.grupo_enemigos.update()
            self.player_1.update()
            self.player_1.draw(self.screen,self.mapas.grupo_bloques,self.enemigo.grupo_enemigos,self.player_1)
            self.mapas.grupo_bloques.draw(self.screen)
            self.mapas.grupo_bloques.update()


            for enemy in self.enemigo.grupo_enemigos:
                enemy.update_animacion(self.screen)

            for fruit in self.fruta.grupo_frutas:
                fruit.update_animacion(self.screen)

            for tramp in self.mapas.grupo_sierras:
                tramp.update_animacion(self.screen)


            contador = self.fuente_1.render(f"Time {str(self.relog)}",True,(255,255,255),(0,0,0))
            contador_vidas = self.fuente_1.render(str(self.player_1.lives),False,(0,0,0))
            contador_score_jugador = self.fuente_1.render(f"Score: {str(self.player_1.score)}",False,(255,255,255),(0,0,0) )
            nivel = self.fuente.render(f"NIVEL: {str(self.nivel + 1)} ESCENARIO: {str(self.escenario + 1)}",False,(255,255,255),(0,0,0) )
            
            self.screen.blit(self.vidas,(80,13))
            self.screen.blit(contador_vidas,(100,30))
            self.screen.blit(contador,(150,30))
            self.screen.blit(contador_score_jugador,(ANCHO_VENTANA-300,30))
            self.screen.blit(nivel,(ANCHO_VENTANA/2,30))

            if self.debug == True:
                print(f" Player X top: {self.player_1.rect.top},left: {self.player_1.rect.left}, right: {self.player_1.rect.right},bottom: {self.player_1.rect.bottom}")
                self.dibujar_bloque()
                self.dibujar_player()
                self.dibujar_frutas()
                self.dibujar_enemigos()
                self.dibujar_balas()
                self.dibujar_sierra()

            self.enemigo.spawn_enemigos(self.screen)

            pg.display.flip()

    def pantalla_final(self):
        if self.player_1.lives == 0:
            self.win = False
        if self.nivel == 2 and self.escenario == 2 and self.player_1.score >= 1000:
            self.win = True

        if self.win != None:
            self.menu_.game_finished(self.win,self.player_1.score)
            
            
    def eleccion_nivel(self, lista_de_niveles,nivel_elegido,escenario_elegido) -> str:
        for numero_de_nivel in range(len(lista_de_niveles)):
            if numero_de_nivel == nivel_elegido:
                nivel = f"level_{numero_de_nivel}"
                level = lista_de_niveles.get(nivel)
                # self.relog = pg.time.get_ticks()

                for escenario in range(len(nivel)- 1):
                    if escenario == escenario_elegido:
                        print(f"nivel : {nivel}, escenario: {escenario}")
                        escenario_a_cargar = level.get(f"{escenario}_escenario")
                        return escenario_a_cargar

    def cargar_mapa(self):
        self.mapa = self.eleccion_nivel(self.lista_de_niveles,self.nivel,self.escenario)
        self.mapas.construir_mapa(self.mapa)

    def cambio_de_escenario(self):
        if self.escenario == 2 and self.player_1.score >= 400  and self.nivel != 2:
            if self.nivel < 2:
                self.nivel += 1
                self.escenario = 0
                game = GameManager(self.nivel,score=self.player_1.score)
                game.tiempo_inicio = pg.time.get_ticks()
                game.run()
                
        elif self.player_1.rect.right > self.screen_width:
            if self.escenario < 2:
                self.escenario += 1
                game = GameManager(self.nivel,escenario=self.escenario, score=self.player_1.score)
                game.run()

                


    def colision_fruta_con_bloque(self,grupo_frutas):
        for objeto in grupo_frutas:
            bloque_colisiona =  pg.sprite.spritecollideany(objeto,self.mapas.grupo_bloques)
            if bloque_colisiona:
            # if self.rect.colliderect(objeto):
                objeto.rect.bottom = bloque_colisiona.rect.top

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
            self.player_1.score += self.fruta.puntos
            print(f"puntos : {self.player_1.score}")
            self.ruido_recompensa.reproducir_audio()

    def colision_con_enemigo(self,objeto):
        if pg.sprite.spritecollide(objeto,self.enemigo.grupo_enemigos,dokill=False):
                if (pg.time.get_ticks() - self.enemigo.tiempo_entre_hits) > self.enemigo.cooldown_de_hit:
                    self.player_1.lives -=1
                    self.enemigo.tiempo_entre_hits = pg.time.get_ticks()

    def colision_con_trampa(self,objeto):
        for tramp in self.mapas.grupo_sierras:
            if objeto.rect.colliderect(tramp.rect):
                    if (pg.time.get_ticks() - self.trampa.tiempo_entre_hits) > self.trampa.cooldown_de_hit:
                        self.player_1.lives -=1
                        self.trampa.tiempo_entre_hits = pg.time.get_ticks()

    def colision_con_objetos(self,player):

        for objeto in self.mapas.grupo_bloques:

            if player.rect.colliderect(objeto):
                objeto = objeto.rect
                if player.rect.bottom > objeto.top and player.rect.top < objeto.top:

                    player.rect.bottom = objeto.top

                elif player.rect.top < objeto.bottom and player.rect.bottom > objeto.bottom:
                    player.rect.top = objeto.bottom


                elif player.rect.right > objeto.left and player.rect.top < objeto.top:
                    player.rect.bottom = objeto.top
                    player.rect.right = objeto.left
                    print(f"parte derecha del personaje: {player.rect.right}, parte izquiera del bloque: {objeto.left}")
                    print("choqué a la derecha")

                elif player.rect.left < objeto.right and player.rect.right > objeto.right:
                    player.rect.bottom = objeto.top
                    player.rect.left = objeto.right
                    print(f"parte izquierda del personaje: {player.rect.left}, parte derecha del bloque: {objeto.right}")
                    print("choqué a la izquiera")




    def dibujar_sierra(self):
        for bloque in self.mapas.grupo_sierras:
            pg.draw.rect(self.screen,"Red",bloque.rect,2)

    def dibujar_bloque(self):
        for bloque in self.mapas.grupo_bloques:
            pg.draw.rect(self.screen,"Black",bloque.rect,2)

    def dibujar_frutas(self):
        for bloque in self.fruta.grupo_frutas:
            pg.draw.rect(self.screen,"Blue",bloque.rect,2)

    def dibujar_enemigos(self):
        for bloque in self.enemigo.grupo_enemigos:
            pg.draw.rect(self.screen,"Red",bloque.rect,2)

    def dibujar_balas(self):
        for bloque in self.player_1.grupo_de_balas:
            pg.draw.rect(self.screen,"White",bloque.rect,2)

    def dibujar_player(self):
            pg.draw.rect(self.screen,"Green",self.player_1.rect,2)

    def volumen_modificar(self):
        volumen_extra = 0.4
        volumen_menos = 0.3

        if self.valor_musica == 0:
            volumen_extra = 0
            volumen_menos = 0.3

        self.ruido_recompensa.set_volumen_audio(self.valor_musica + volumen_extra)
        self.musica_de_fondo.set_volumen_audio(self.valor_musica - volumen_menos)
# 
