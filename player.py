import pygame as pg
from auxiliar import Auxiliar
from constantes import *



class Player(pg.sprite.Sprite):
    def __init__(self, diccionario) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1, True)[:12]
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Idle (32x32).png", 11, 1)
        # self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, False, 2)
        # self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, True, 2)
        self.frame = 0
        self.lives = 5
        self.score = 0
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

        self.is_jump = False


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
        if not movimientos[pg.K_RIGHT] and not movimientos[pg.K_LEFT]:
            self.control("STAY")




    def control(self, action):
        if action == "WALK_R":
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
            self.direccion = "right"


        elif action == "WALK_L":
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
            self.direccion = "left"

        elif action == "JUMP_R":
            self.move_y = -self.jump
            self.move_x = self.speed_walk
            # self.animation = self.jump_r
            # self.frame = 0
            self.direccion = "up"
            self.is_jump = True

        elif action == "JUMP_L":
            self.move_y = -self.jump
            self.move_x = -self.speed_walk
            # self.animation = self.jump_l
            # self.frame = 0
            self.direccion = "up"
            self.is_jump = True

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

    # def colision_con_enemigo(self,objeto):
    #     if pg.sprite.spritecollide(objeto,self.grupo_enemigos):
    #         if self.rect.colliderect(objeto):
    #             if objeto.rect.bottom < self.rect.top:
    #                 print("pisó al enemigo")
    #             else:
    #                 if (pg.time.get_ticks() - self.tiempo_entre_hits) > self.cooldown_de_hit:
    #                     self.lives -=1
    #                     self.tiempo_entre_hits = pg.time.get_ticks()


    def movimiento_horizontal_de_la_camara(self, valor):
        camara_x = -self.rect[0] % ANCHO_VENTANA
        camara_x -=  valor
        return camara_x


    # def colision_con_objetos(self,objeto):
    #     if pg.sprite.spritecollide(self.rect,):
    #     # if self.rect.colliderect(objeto):
    #         if self.rect[1] < objeto.top:
    #             # print("choqué abajo")
    #             self.rect.bottom = objeto.top

    #         elif self.rect[1] < objeto.bottom and self.rect.bottom > objeto.bottom:
    #             self.rect.top = objeto.bottom
    #             print("choqué arriba")
    #         elif self.rect[0] < objeto.left:
    #             self.rect.right = objeto.left
    #             # print("choqué a la derecha")
    #         elif self.rect[0] <= objeto.right:
    #             self.rect.left = objeto.right
    #             # print("choqué a la izquiera")





    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

