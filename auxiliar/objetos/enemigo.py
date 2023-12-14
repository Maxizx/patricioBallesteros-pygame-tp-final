
import pygame as pg
from auxiliar.constantes import *
from auxiliar.auxiliar import Auxiliar
import random as rd
from auxiliar.musica import Audio



class Enemy(pg.sprite.Sprite):
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.image_R = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/Chicken/Run (32x34).png", 14, 1,True)[:14]
        self.image_L = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/Chicken/Run (32x34).png", 14, 1,False)[:14]
        self.image_spawner = Auxiliar.load_image_and_scale("images/caracters/stink/Fall (32x32).png",100,110)
        self.live = 100
        self.frame = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk = rd.randint(2,5)
        self.speed_run = rd.randint(2,5)
        self.gravity = 8
        self.move_x += self.speed_walk
        self.animation = self.image_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.mira_a_la_derecha = True
        self.grupo_enemigos = pg.sprite.Group()
        self.cooldown_de_hit = 1000
        self.tiempo_entre_hits =pg.time.get_ticks()
        self.tiempo_spawn= 8000
        self.relog_spawn = pg.time.get_ticks()
        self.ruido_spawn = Audio("generador_gallinas")



    def caminar_direccion(self, izquierda = True):
        if izquierda == True:
            self.move_x = -self.speed_walk
        else:
            self.move_x = self.speed_walk

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0

        if self.rect[0] < 0:
            self.rect[0] = 0
            self.move_x = self.move_x*-1
            self.mira_a_la_derecha = True


        elif self.rect[0] > ANCHO_VENTANA:
            self.rect[0] = ANCHO_VENTANA
            self.move_x = self.move_x * -1
            self.mira_a_la_derecha = False



        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.y < ALTO_VENTANA:
            self.rect.y += self.gravity

    def quitar_vida(self,daño):
        self.live -= daño
        return self.live

    def spawn_enemigos(self,screen, cantidad_de_enemigos = 4, coodenadas_x = 0, coodenadas_y = 0):
        screen.blit(self.image_spawner,(coodenadas_x,coodenadas_y))
        if (pg.time.get_ticks() - self.relog_spawn) > self.tiempo_spawn:
            for _ in range(cantidad_de_enemigos):
                    enemigo = Enemy(coodenadas_x,coodenadas_y)
                    self.grupo_enemigos.add(enemigo)
                    print("Se creó un enemigo nueva")
                    self.ruido_spawn.reproducir_audio()
            self.relog_spawn = pg.time.get_ticks()
    

    def update_animacion(self,screen):
        if self.mira_a_la_derecha == True:
            self.animation = self.image_R
        elif self.mira_a_la_derecha == False:
            self.animation = self.image_L
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


