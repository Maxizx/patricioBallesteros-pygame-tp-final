import sys
import pygame as pg
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from auxiliar.constantes import (ANCHO_VENTANA,ALTO_VENTANA)
from interfaz.settings.botones import Button as Button
from auxiliar.auxiliar import Auxiliar
from base_de_datos.bd_ranking import base_de_datos


# if __name__ == "__main__":
class menu():
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pg.display.set_caption("Menu")
        self.BG = pg.image.load("images/locations/fondos/Purple.png")
        self.BG = pg.transform.scale(self.BG, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rescalado = (800,400)
        self.panel_menu_niveles = Auxiliar.load_image_and_scale("images/UI/PNG/blue_panel.png",medida_del_ancho = self.rescalado[0],medida_de_lo_alto=self.rescalado[1])
        # self.panel_menu_niveles = pg.transform.scale(self.panel_menu_niveles,(self.rescalado))
        self.posicion_del_mouse = pg.mouse.get_pos()
        self.x_centrada= ANCHO_VENTANA/2
        self.posicion_titulo = (self.x_centrada,100)
        self.posicion_centrada = (self.x_centrada, ALTO_VENTANA/2)
        self.posicion_centrada_abajo = (self.x_centrada, (ALTO_VENTANA/2)+100)
        self.color_boton = "Black"
        self.color_boton_al_apretar = "White"
        self.color_letras = "Black"
        self.volumen_actual = 0.2
        self.bd = base_de_datos()
        self.titulo = "YOU LOSE GAME OVER"
        self.color = "Red"


    def output(self):
        string = self.textbox.getText()
        return string

    def get_font(self,size): 
        return pg.font.Font("images/UI/Font/kenvector_future_thin.ttf", size)
        
    def game_finished(self,win,score):
        self.textbox = TextBox(self.screen, 100, 250, 800, 80, fontSize=50,
                borderColour=(255, 0, 0), textColour=(0, 200, 0),
                onSubmit=self.output, radius=10, borderThickness=5)
        puntaje = score
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()

            self.screen.fill("black")
            if win == True:
                self.titulo = "YOU WON GAME OVER"
                self.color = "Green"

            
            self.PLAY_TEXT = self.get_font(70).render(self.titulo, True, self.color )
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= (self.posicion_centrada[0],self.posicion_centrada[1]-200))
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)

            self.PLAY_BACK = Button(image=None, pos= (self.posicion_centrada_abajo[0],self.posicion_centrada_abajo[1] + 100), 
                                text_input="Rank", font=self.get_font(75), base_color="White", hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        nombre = self.output()
                        self.bd.ranking(nombre,puntaje)

            pygame_widgets.update(events)
            pg.display.update()

    def pause(self):
        pausa = True
        slider = Slider(self.screen,400,350,500,20,min=0,max=99,step=1)
        slider.setValue(int(self.volumen_actual * 100))
        output = TextBox(self.screen, 940, 340, 35, 35, fontSize=20)
        
        while pausa:
            self.posicion_del_mouse = pg.mouse.get_pos()
            # self.screen.fill("black")
            self.screen.blit(self.BG, (0,0))

            output.setText(slider.getValue())
            valor = slider.getValue() / 100

            self.volumen_actual = valor



            


            self.PLAY_TEXT = self.get_font(45).render("Pause", True, "White")
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= (self.x_centrada,200))

            self.PLAY_TEXT = self.get_font(45).render("Pause", True, "White")
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= (self.posicion_centrada_abajo[0],200))
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)


            self.PLAY_BACK = Button(image=None, pos=self.posicion_centrada_abajo, 
                                text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)

            lista_de_eventos = pg.event.get()
            for event in lista_de_eventos:
                if event.type == pg.QUIT:
                    pg.quit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        pausa = False
                        return self.volumen_actual

            pygame_widgets.update(lista_de_eventos)

            pg.display.update() 

    def options(self):
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()
            self.screen.fill("white")

            self.OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS self.screen.", True, "Black")
            self.OPTIONS_RECT = self.OPTIONS_TEXT.get_rect(center= self.posicion_centrada)
            self.screen.blit(self.OPTIONS_TEXT, self.OPTIONS_RECT)

            self.OPTIONS_BACK = Button(image=None, pos=self.posicion_centrada_abajo, 
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            self.OPTIONS_BACK.changeColor(self.posicion_del_mouse)
            self.OPTIONS_BACK.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.OPTIONS_BACK.checkForInput(self.posicion_del_mouse):
                        self.main_menu()

            pg.display.update()

