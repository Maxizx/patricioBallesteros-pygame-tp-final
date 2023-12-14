import pygame as pg
from auxiliar.auxiliar import Auxiliar
from auxiliar.constantes import *
from auxiliar.objetos.balas import balas
from auxiliar.musica import Audio


class Player(pg.sprite.Sprite):
    def __init__(self, diccionario,score,lives) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1, True)[:12]
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Idle (32x32).png", 11, 1)
        # self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, False, 2)
        # self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, True, 2)
        self.frame = 0
        self.lives = lives
        self.score = score
        self.move_x = diccionario["x"]
        self.move_y = diccionario["y"]
        self.speed_walk = diccionario["speed_walk"]
        self.speed_run = diccionario["speed_run"]
        self.gravity = diccionario["gravity"]
        self.jump = diccionario["jump"]
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.direccion = "right"
        self.cooldown_de_hit = 1000
        self.tiempo_entre_hits = pg.time.get_ticks()
        self.grupo_de_balas = pg.sprite.Group()
        self.lado = False
        self.is_jump = False
        self.cooldown_disparo = 150         
        self.tiempo_entre_disparos = pg.time.get_ticks()
        self.ruido_disparo = Audio("pop")
        self.ruido_salto = Audio("jump")




    def selector_de_movimiento(self,movimientos):
        # if event.type == pg.KEYDOWN:
        if movimientos[pg.K_LEFT] and not movimientos[pg.K_RIGHT]:
            self.control("WALK_L")
        if movimientos[pg.K_RIGHT] and not movimientos[pg.K_LEFT]:
            self.control("WALK_R")
        if movimientos[pg.K_SPACE]:
            self.control("JUMP_R")
        if movimientos[pg.K_SPACE] and movimientos[pg.K_LEFT]:
            self.control("JUMP_L")
        if movimientos[pg.K_a]:
            self.control("ATTACK")
        if not movimientos[pg.K_RIGHT] and not movimientos[pg.K_LEFT]:
            self.control("STAY")




    def control(self, action):
        if action == "ATTACK":
            if (pg.time.get_ticks() - self.tiempo_entre_disparos) > self.cooldown_disparo:
                self.tiempo_entre_disparos = pg.time.get_ticks()
                bala = balas("images/huevo.png",self.rect.x,self.rect.y,self.speed_run,self.lado)
                self.grupo_de_balas.add(bala)
                self.ruido_disparo.reproducir_audio()




        if action == "WALK_R":
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
            self.direccion = "right"
            self.lado = True


        elif action == "WALK_L":
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
            self.direccion = "left"
            self.lado = False

        elif action == "JUMP_R":
            self.move_y = -self.jump
            self.move_x = self.speed_walk
            # self.animation = self.jump_r
            # self.frame = 0
            self.direccion = "up"
            self.is_jump = True
            self.ruido_salto.reproducir_audio()

        elif action == "JUMP_L":
            self.move_y = -self.jump
            self.move_x = -self.speed_walk
            # self.animation = self.jump_l
            # self.frame = 0
            self.direccion = "up"
            self.is_jump = True
            self.ruido_salto.reproducir_audio()


        elif action == "STAY":
            self.animation = self.stay
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
            if self.is_jump == True:
                self.is_jump = False
                self.move_y = 0
                self.direccion = "down"
        
        if self.rect[0] < 0:
            self.rect[0] = 0

        elif self.rect[0] > ANCHO_VENTANA:
            self.rect[0] = 0


        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.y < ALTO_VENTANA:
            self.rect.y += self.gravity
        elif self.rect.y > ALTO_VENTANA:
            print("se cayó fuera del mapa")
            self.rect.y -= self.rect.y
            self.rect.x -= self.rect.x
            self.lives -= 1

    def draw(self, screen,grupo1 , grupo2,player):
        for bala in self.grupo_de_balas:
            bala.draw(screen,grupo1,grupo2,player)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


