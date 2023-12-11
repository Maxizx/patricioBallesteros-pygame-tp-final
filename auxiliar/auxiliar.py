import pygame as pg


class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip=False, step=1):
        lista = []
        surface_imagen = pg.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width() / columnas)
        fotograma_alto = int(surface_imagen.get_height() / filas)
        x = 0
        for columna in range(0, columnas, step):
            for fila in range(filas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(
                    x, y, fotograma_ancho, fotograma_alto
                )
                if flip:
                    surface_fotograma = pg.transform.flip(
                        surface_fotograma, True, False
                    )
                lista.append(surface_fotograma)
        return lista


    @staticmethod
    def get_image_SurfaceFromSpriteSheet(path, columnas, filas,seleccion_columna ,seleccion_fila, step=1):
        """  
        Obtener una imagen de un spritsheet
        """
        
        imagen = None
        surface_imagen = pg.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width() / columnas)
        fotograma_alto = int(surface_imagen.get_height() / filas)
        x = 0
        for columna in range(0, columnas, step):
            if columna == seleccion_columna:

                for fila in range(filas):
                    if fila == seleccion_fila:
                        x = columna * fotograma_ancho
                        y = fila * fotograma_alto
                        surface_fotograma = surface_imagen.subsurface(
                            x, y, fotograma_ancho, fotograma_alto
                        )
                        imagen = surface_fotograma
        return imagen


    def load_image_and_scale(ruta:str, medida_del_ancho:int, medida_de_lo_alto:int):
        """  
        Recibe como parametro la ruta en donde se ubica el archivo, las medidas de alto como de ancho que se desea.
         Carga una imagen y la reescala a las medidas cargas por paremetros. 
          -> retorna la imagen reescalada
        """
        imagen_carga = pg.image.load(ruta)
        medidas_para_escalar= (medida_del_ancho,medida_de_lo_alto)
        imagen_escalada = pg.transform.scale(imagen_carga,medidas_para_escalar)
        
        return imagen_escalada
    

