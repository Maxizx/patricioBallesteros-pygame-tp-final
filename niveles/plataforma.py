import pygame as pg
#from pg.sprite import _Group
from auxiliar import Auxiliar
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
        self.grupo_bloques = pg.sprite.Group()


    def draw_bloque(self, pantalla):
            for ubi in range(50,1000,self.rect.width - 2):
                self.rect.x = ubi
                self.rect.y = coordenadas_y
                pantalla.blit(self.imagen_del_bloque, self.rect)

    def draw_bloque(self, pantalla):
        pantalla.blit(self.imagen_del_bloque, self.rect)

# nivel = niveles.get("nivel_1")

def eleccion_nivel(lista_de_niveles,nivel_elegido,escenario_elegido) -> str:
    for numero_de_nivel in range(len(lista_de_niveles)):
        if numero_de_nivel == nivel_elegido:
            nivel = f"level_{numero_de_nivel}"
            level = lista_de_niveles.get(nivel)

            for escenario in range(len(nivel)- 1):
                if escenario == escenario_elegido:
                    print(f"nivel : {nivel}, escenario: {escenario}")
                    escenario_a_cargar = level.get(f"{escenario}_escenario")
                    return escenario_a_cargar


bloque_de_abajo = bloque()

def dibujar_muro(superficie, rectangulo):

    # pg.draw.rect(superficie, (0,0,0), rectangulo)
    superficie.blit(bloque_de_abajo.imagen_del_bloque,bloque_de_abajo.imagen_del_bloque.get_rect(topleft = (rectangulo.x,rectangulo.y)))

def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for muro in mapa:
        for ladrillo in muro:
            if ladrillo == "X":
                muros.append(pg.Rect(x, y, 60, 60))
            x += bloque_de_abajo.imagen_del_bloque.get_width()
        x = 0
        y += bloque_de_abajo.imagen_del_bloque.get_height()
    return muros

def dibujar_muros(superficie, muros):
    for m in muros:
        dibujar_muro(superficie, m)


mapa = eleccion_nivel(niveles,0,2)

muros = construir_mapa(mapa)




