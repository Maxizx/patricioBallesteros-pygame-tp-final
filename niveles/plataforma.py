import pygame as pg
from constantes import *



#plataforma_uno= pg.image.load("images/locations/Terrain (16x16).png")
# plataforma_uno= Auxiliar.get_image_SurfaceFromSpriteSheet("images/locations/Terrain (16x16).png", 4, 3)

# plataforma_rect = plataforma_uno[0].get_rect()



# def draw_objeto(pantalla):
#     for ubi in range(50,1000,plataforma_rect.width):
#         pantalla.blit(plataforma_uno[0], plataforma_uno[0].get_rect(topleft=( ubi,coordenadas_y)))

coordenadas_x = 200
coordenadas_y = 400

class bloque(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.imagen_del_bloque = pg.image.load("images/locations/0.png")
        # self.imagen_del_bloque = Auxiliar.get_image_SurfaceFromSpriteSheet("images/locations/Terrain (16x16).png",4,3,seleccion_columna=1,seleccion_fila=0,step=1)
        self.rect = self.imagen_del_bloque.get_rect()


    def draw_bloque(self, pantalla):
            for ubi in range(50,1000,self.rect.width - 2):
                self.rect.x = ubi
                self.rect.y = coordenadas_y
                pantalla.blit(self.imagen_del_bloque, self.rect)

    def draw_bloque(self, pantalla):
        pantalla.blit(self.imagen_del_bloque, self.rect)

# nivel = niveles.get("nivel_1")


class construir_mapas(bloque,pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.bloque_plataforma = bloque()
        self.grupo_bloques = pg.sprite.Group()


    def dibujar_muro(self,superficie, rectangulo):

        # pg.draw.rect(superficie, (0,0,0), rectangulo)
        superficie.blit(self.bloque_plataforma.imagen_del_bloque,self.bloque_plataforma.imagen_del_bloque.get_rect(topleft = (rectangulo.x,rectangulo.y)))
        # for valor in rectangulo.values():
        #     superficie.blit(self.bloque_plataforma.imagen_del_bloque,self.bloque_plataforma.imagen_del_bloque.get_rect(topleft = (valor["x"],valor["y"])))

    def construir_mapa(self,mapa):
        muros = []
        x = 0
        y = 0
        for muro in mapa:
            for ladrillo in muro:
                diccionario = {}
                if ladrillo == "X":
                    muros.append(pg.Rect(x, y, 60, 60))
                    # diccionario["x"] = x
                    # diccionario["y"] = y

                    # muros.append(diccionario)
                    # self.grupo_bloques.add(muro)
                x += self.bloque_plataforma.imagen_del_bloque.get_width()
            x = 0
            y += self.bloque_plataforma.imagen_del_bloque.get_height()
        return muros

    def dibujar_muros(self,superficie, muros):
        for m in muros:
            self.dibujar_muro(superficie, m)


# mapa = eleccion_nivel(niveles,0,escenario)

# muros = construir_mapa(mapa)




