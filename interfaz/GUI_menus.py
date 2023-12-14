import pygame as pg
import pygame_widgets
import sys
from auxiliar.constantes import (ANCHO_VENTANA,ALTO_VENTANA)
from interfaz.settings.botones import Button as Button
from auxiliar.auxiliar import Auxiliar
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


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




    def get_font(self,size): # Returns Press-Start-2P in the desired size
        return pg.font.Font("images/UI/Font/kenvector_future_thin.ttf", size)
        
    def game_over(self):
        over = True
        while over:
            self.posicion_del_mouse = pg.mouse.get_pos()

            self.screen.fill("black")
            self.PLAY_TEXT = self.get_font(70).render("Gave Over", True, (255,45,0))
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= self.posicion_centrada)
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)

            self.PLAY_BACK = Button(image=None, pos= self.posicion_centrada_abajo, 
                                text_input="SALIR", font=self.get_font(75), base_color="White", hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        # over = False
                        pg.quit()
                        sys.exit()

            pg.display.update()

    def win_game(self):
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()

            self.screen.fill("black")
            self.PLAY_TEXT = self.get_font(70).render("Win", True, "Green")
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= self.posicion_centrada)
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)

            self.PLAY_BACK = Button(image=None, pos= self.posicion_centrada_abajo, 
                                text_input="SALIR", font=self.get_font(75), base_color="White", hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        pg.quit()
                        sys.exit()

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

