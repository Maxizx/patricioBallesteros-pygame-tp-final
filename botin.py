import pygame as pg
import random
from auxiliar import Auxiliar
import random as rd
from constantes import (ANCHO_VENTANA,ALTO_VENTANA)

class Frutas(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/Apple.png",17,1,step=1)
        self.puntos = random.randrange(10,50)
        self.frame = 0
        # self.ubicacion_en_x = x
        # self.ubicacion_en_y = y
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0,ANCHO_VENTANA - self.rect.width)
        self.rect.y = rd.randint(0,ALTO_VENTANA - self.rect.height)
        self.grupo_frutas = pg.sprite.Group()

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
    
    def spawn_frutas(self,cantidad_de_frutas = 4):
        for _ in range(cantidad_de_frutas):
            fruta = Frutas()
            self.grupo_frutas.add(fruta)
            # print(f"x: {fruta.rect.x} y :{fruta.rect.y}")
            print("Se creó una fruta nueva")
            

        
    # def draw(self,pantalla):
    #     self.image = self.animation[self.frame]
    #     pantalla.blit(self.image,self.rect)

    # def colision_con_fruta(self,objeto):
    #     if pg.sprite.spritecollide(objeto,group = self.grupo_frutas,dokill = True):
    #     # if self.rect.colliderect(objeto):
    #         print("frutaaa")
    #         print(self.puntos)