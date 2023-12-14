import pygame as pg
from auxiliar.auxiliar import Auxiliar
from auxiliar.constantes import *
from auxiliar.musica import Audio


class balas(pg.sprite.Sprite):
    def __init__(self, path_sprite_pj, x, y, speed,lado):
        pg.sprite.Sprite.__init__(self)
        self.daño = 20
        self.lado = lado
        self.sprite_pj = Auxiliar.getSurfaceFromSpriteSheet(path_sprite_pj, 8, 1,self.lado,rescalar=0.25)
        self.index_current_frame = 0
        self.current_frame = self.sprite_pj[self.index_current_frame]
        self.rect = self.current_frame.get_rect()
        self.rect.centerx = x 
        self.rect.bottom = y + 10
        self.update_time = pg.time.get_ticks()
        self.frames = 85
        self.ruido_kill = Audio("kill_chicken")


        if self.lado == False:
            self.speed = speed * -1
        else:
            self.speed = speed

        
    def update(self, lista_de_obstaculos, lista_de_enemigos,player):

        self.rect.centerx += self.speed

        self.colision_con_bloques(lista_de_obstaculos)
        self.colision_con_enemigo(lista_de_enemigos,player)
        self.colision_bordes()


    def colision_bordes(self):
            if self.rect.centerx > ANCHO_VENTANA or self.rect.centerx < 0:
                self.kill()

    def colision_con_enemigo(self, lista_de_enemigos,player):
        for enemigo in lista_de_enemigos:
            if enemigo.rect.colliderect(self.rect):
                vida_enemigo = enemigo.quitar_vida(self.daño)
                print(vida_enemigo)
                if vida_enemigo <= 0:
                    enemigo.kill()
                    player.score += 10
                    self.ruido_kill.reproducir_audio()

                self.kill()
                
    
    def colision_con_bloques(self, obstacle_group):
        for obstacle in obstacle_group:
            if obstacle.rect.colliderect(self.rect):
                self.kill()
                
    def do_animation(self):
        self.current_frame = self.sprite_pj[self.index_current_frame]
        if pg.time.get_ticks() - self.update_time > self.frames:
            if self.index_current_frame < len(self.sprite_pj) -1:
                self.index_current_frame += 1
            else:
                self.index_current_frame = 0
            self.update_time = pg.time.get_ticks()
        
    def draw(self, screen,lista_de_obstaculos, lista_de_enemigos,player):
        self.update(lista_de_obstaculos, lista_de_enemigos,player)
        self.do_animation()
        screen.blit(self.current_frame, (self.rect.centerx,self.rect.centery))

