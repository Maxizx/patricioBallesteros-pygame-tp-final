import pygame as pg
import random
from auxiliar.auxiliar import Auxiliar
import random as rd
from auxiliar.constantes import (ANCHO_VENTANA,ALTO_VENTANA)

class Frutas(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Auxiliar.getSurfaceFromSpriteSheet("images/Apple.png",17,1,step=1)
        self.puntos = random.randrange(15,30)
        self.frame = 0
        self.animation = self.image
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0,ANCHO_VENTANA - self.rect.width)
        self.rect.y = rd.randint(0,ALTO_VENTANA / 2 - self.rect.height)
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

    def update_animacion(self,screen):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

        
    # def draw(self,pantalla):
    #     self.image = self.animation[self.frame]
    #     pantalla.blit(self.image,self.rect)

    # def colision_con_fruta(self,objeto):
    #     if pg.sprite.spritecollide(objeto,group = self.grupo_frutas,dokill = True):
    #     # if self.rect.colliderect(objeto):
    #         print("frutaaa")
    #         print(self.puntos)