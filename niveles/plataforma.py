import pygame as pg
from auxiliar.constantes import *
from auxiliar.auxiliar import Auxiliar

class sierra(pg.sprite.Sprite):
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.image = Auxiliar.getSurfaceFromSpriteSheet("images/On (38x38).png", 8, 1)
        self.daño = 1
        self.frame = 0
        self.animation = self.image
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(center=(x,y))
        self.direccion = "right"
        self.cooldown_de_hit = 1000
        self.tiempo_entre_hits =pg.time.get_ticks()


    def update_animacion(self,screen):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


class construir_mapas(pg.sprite.Sprite):
    def __init__(self,x = 0,y = 0) -> None:
        super().__init__()
        self.image = pg.image.load("images/locations/0.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grupo_bloques = pg.sprite.Group()
        self.grupo_sierras = pg.sprite.Group()

    def construir_mapa(self,mapa):
        x = 0
        y = 0
        for muro in mapa:
            for ladrillo in muro:
                if ladrillo == "X":
                    bloque_plataforma = construir_mapas(x,y)
                    self.grupo_bloques.add(bloque_plataforma)
                if ladrillo == "O":
                    trampa = sierra(x,y)
                    self.grupo_sierras.add(trampa)

                x += self.image.get_width()
            x = 0
            y += self.image.get_height()
        



