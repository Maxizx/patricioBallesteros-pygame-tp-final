import pygame as pg
import random
import player
from auxiliar import Auxiliar

class Frutas(pg.sprite.Sprite):
    def __init__(self,x,y ) -> None:
        super().__init__()
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/Apple.png",17,1,step=1)
        self.puntos = random.randrange(10,50)
        self.frame = 0
        self.ubicacion_en_x = x
        self.ubicacion_en_y = y
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0


        
    def draw(self,pantalla):
        self.rect.x = self.ubicacion_en_x
        self.rect.y = self.ubicacion_en_y
        self.image = self.animation[self.frame] 
        pantalla.blit(self.image,self.rect)

    def colision_con_fruta(self,objeto):
        if self.rect.colliderect(objeto):
            print(self.puntos)