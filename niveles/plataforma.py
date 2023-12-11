import pygame as pg
from auxiliar.constantes import *
from auxiliar.auxiliar import Auxiliar



#plataforma_uno= pg.image.load("images/locations/Terrain (16x16).png")
# plataforma_uno= Auxiliar.get_image_SurfaceFromSpriteSheet("images/locations/Terrain (16x16).png", 4, 3)

# plataforma_rect = plataforma_uno[0].get_rect()



# def draw_objeto(pantalla):
#     for ubi in range(50,1000,plataforma_rect.width):
#         pantalla.blit(plataforma_uno[0], plataforma_uno[0].get_rect(topleft=( ubi,coordenadas_y)))

coordenadas_x = 200
coordenadas_y = 400

class bloque(pg.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.imagen_del_bloque = pg.image.load("images/locations/0.png")
        # self.imagen_del_bloque = Auxiliar.get_image_SurfaceFromSpriteSheet("images/locations/Terrain (16x16).png",4,3,seleccion_columna=1,seleccion_fila=0,step=1)
        self.rect = self.imagen_del_bloque.get_rect()
        self.rect.x = x
        self.rect.y = y


    # def draw_bloque(self, pantalla):
    #         for ubi in range(50,1000,self.rect.width - 2):
    #             self.rect.x = ubi
    #             self.rect.y = coordenadas_y
    #             pantalla.blit(self.imagen_del_bloque, self.rect)

    # def draw_bloque(self, pantalla):
    #     pantalla.blit(self.imagen_del_bloque, self.rect)

# nivel = niveles.get("nivel_1")


class construir_mapas(pg.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pg.image.load("images/locations/0.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grupo_bloques = pg.sprite.Group()

    def construir_mapa(self,mapa):
        x = 0
        y = 0
        for muro in mapa:
            for ladrillo in muro:
                if ladrillo == "X":
                    bloque_plataforma = construir_mapas(x,y)
                    self.grupo_bloques.add(bloque_plataforma)

                x += self.image.get_width()
            x = 0
            y += self.image.get_height()
        



