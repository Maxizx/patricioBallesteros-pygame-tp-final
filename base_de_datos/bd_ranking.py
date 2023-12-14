import sqlite3
import pygame as pg
from interfaz.settings.botones import Button 
from auxiliar.constantes import (ANCHO_VENTANA,ALTO_VENTANA)
from auxiliar.auxiliar import Auxiliar



class base_de_datos:
    def __init__(self) -> None:
        self.nombre_del_archivo = "bd_sqlite.db"
        self.screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        self.posicion_titulo = (ANCHO_VENTANA/2,100)
        self.rescalado = (800,400)
        self.panel_menu_niveles = Auxiliar.load_image_and_scale("images/UI/PNG/blue_panel.png",medida_del_ancho = self.rescalado[0],medida_de_lo_alto=self.rescalado[1])
        self.color_boton_al_apretar = "Green"
        self.color_letras="Black"


    def crear_tabla(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
                conexion.execute("create table if not exists ranking (player TEXT,score INTEGER);")

    def agregar_datos(self,player,score):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            conexion.execute("insert into ranking(player,score) values (?,?)", (player,score))
            conexion.commit()#

    def recibir_datos(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            cursor = conexion.execute("SELECT player, score FROM ranking ORDER BY score DESC LIMIT 5;")
            lista = []
            for fila in cursor:
                lista.append(fila)
            return lista

    def get_font(self,size): # Returns Press-Start-2P in the desired size
            return pg.font.Font("images/UI/Font/kenvector_future_thin.ttf", size)
        
    def ranking(self, player,score):
        self.crear_tabla()
        self.agregar_datos(player,score)
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()
            self.screen.fill("black")

            self.PLAY_TEXT = self.get_font(45).render("RANKING", True, self.color_boton_al_apretar)
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= self.posicion_titulo)
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)
            self.screen.blit(self.panel_menu_niveles,(250, 160))

            datos = self.recibir_datos()
            print(datos)

            self.PLAY_BACK = Button(image="images/UI/PNG/grey_button02.png", pos=(640,630), text_input="BACK", font=self.get_font(75), base_color=self.color_letras, hovering_color="Green")
            self.level_one = Button(image="images/UI/PNG/grey_button02.png", pos=(ANCHO_VENTANA/2,250), text_input=" LEVEL 1 ", font=self.get_font(75), base_color = self.color_letras, hovering_color="Green")
            self.level_two = Button(image="images/UI/PNG/grey_button02.png", pos=(ANCHO_VENTANA/2,350), text_input=" LEVEL 2 ", font=self.get_font(75), base_color = self.color_letras, hovering_color="Green")
            self.level_three = Button(image="images/UI/PNG/grey_button02.png", pos=(ANCHO_VENTANA/2,450), text_input=" LEVEL 3 ", font=self.get_font(75), base_color =  self.color_letras, hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.level_one.changeColor(self.posicion_del_mouse)
            self.level_two.changeColor(self.posicion_del_mouse)
            self.level_three.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)
            self.level_one.update(self.screen)
            self.level_two.update(self.screen)
            self.level_three.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        self.main_menu()
                    if self.level_one.checkForInput(self.posicion_del_mouse):
                        pass
                    if self.level_two.checkForInput(self.posicion_del_mouse):
                        pass
                    if self.level_three.checkForInput(self.posicion_del_mouse):
                        pass


            pg.display.update()
        
