
import pygame as pg
from auxiliar.constantes import *
from auxiliar.auxiliar import Auxiliar
from auxiliar.constantes import *
from auxiliar.objetos.player import Player
import random as rd


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1, True)[:12]
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Idle (32x32).png", 11, 1)
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk = rd.randint(2,5)
        self.speed_run = rd.randint(2,5)
        self.gravity = 8
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.direccion = "right"
        self.grupo_enemigos = pg.sprite.Group()
        self.cooldown_de_hit = 1000
        self.tiempo_entre_hits = pg.time.get_ticks()
        self.move_x += self.speed_walk
        self.tiempo_spawn= 6000
        self.relog_spawn = pg.time.get_ticks()



    def caminar_direccion(self, izquierda = True):
        if izquierda == True:
            # Enemy.control("WALK_L")
            self.move_x = -self.speed_walk
        else:
            # Enemy.control("WALK_R")
            self.move_x = self.speed_walk

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0

        if self.rect[0] < 0:
            self.rect[0] = 0
            self.caminar_direccion(False)

        elif self.rect[0] > ANCHO_VENTANA:
            self.rect[0] = ANCHO_VENTANA
            self.caminar_direccion(True)


        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.y < ALTO_VENTANA:
            self.rect.y += self.gravity

    def movimiento_horizontal_de_la_camara(self, valor):
        camara_x = -self.rect[0] % ANCHO_VENTANA
        camara_x -=  valor
        return camara_x

    # def colision_con_enemigo(self,objeto):
    #     if pg.sprite.spritecollide(objeto,self.grupo_enemigos,dokill=False):
    #         # if self.rect.colliderect(objeto):
    #             if (pg.time.get_ticks() - self.tiempo_entre_hits) > self.cooldown_de_hit:
    #                 self.heroe.lives -=1
    #                 self.tiempo_entre_hits = pg.time.get_ticks()

    # def colision_con_objetos(self,objeto):

    #     if self.rect.colliderect(objeto):
    #         if self.rect[1] < objeto.top:
    #             self.rect.bottom = objeto.top
    #         elif self.rect[0] < objeto.left:
    #             self.rect.right = objeto.left
    #             self.caminar_direccion(True)
    #         elif self.rect[0] <= objeto.right:
    #             self.rect.left = objeto.right
    #             self.caminar_direccion(False)

    def spawn_enemigos(self,cantidad_de_enemigos = 4):
        if (pg.time.get_ticks() - self.relog_spawn) > self.tiempo_spawn:
            for _ in range(cantidad_de_enemigos):
                    enemigo = Enemy(0,0)
                    self.grupo_enemigos.add(enemigo)
                    print("Se creó un enemigo nueva")
            self.relog_spawn = pg.time.get_ticks()
    
        