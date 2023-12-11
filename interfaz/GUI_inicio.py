import pygame as pg
from auxiliar.constantes import (ANCHO_VENTANA,ALTO_VENTANA)
from interfaz.botones import Button as Button
from game import GameManager
from auxiliar.auxiliar import Auxiliar
from interfaz.GUI_menus import menu

# if __name__ == "__main__":
class GUI():
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

    def get_font(self,size): # Returns Press-Start-2P in the desired size
        return pg.font.Font("images/UI/Font/kenvector_future_thin.ttf", size)
        
    def niveles(self):
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()
            self.screen.fill("black")

            self.PLAY_TEXT = self.get_font(45).render("Selecciona tu nivel.", True, self.color_boton_al_apretar)
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= self.posicion_titulo)
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)
            self.screen.blit(self.panel_menu_niveles,(250, 160))

            self.PLAY_BACK = Button(image="images/UI/PNG/grey_button02.png", pos=(640,630), text_input="BACK", font=self.get_font(75), base_color=self.color_letras, hovering_color="Green")
            self.level_one = Button(image="images/UI/PNG/grey_button02.png", pos=(self.x_centrada,250), text_input=" LEVEL 1 ", font=self.get_font(75), base_color = self.color_letras, hovering_color="Green")
            self.level_two = Button(image="images/UI/PNG/grey_button02.png", pos=(self.x_centrada,350), text_input=" LEVEL 2 ", font=self.get_font(75), base_color = self.color_letras, hovering_color="Green")
            self.level_three = Button(image="images/UI/PNG/grey_button02.png", pos=(self.x_centrada,450), text_input=" LEVEL 3 ", font=self.get_font(75), base_color =  self.color_letras, hovering_color="Green")

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
                        self.game_level = 0
                    if self.level_two.checkForInput(self.posicion_del_mouse):
                        self.game_level = 1
                    if self.level_three.checkForInput(self.posicion_del_mouse):
                        self.game_level = 2

                    self.game = GameManager(self.game_level)
                    self.game.run()

            pg.display.update()
        
    def play(self):
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()
            self.screen.fill("black")

            self.PLAY_TEXT = self.get_font(45).render("This is the PLAY self.screen.", True, "White")
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center= self.posicion_centrada)
            self.screen.blit(self.PLAY_TEXT, self.PLAY_RECT)

            self.PLAY_BACK = Button(image=None, pos=self.posicion_centrada_abajo, text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            self.PLAY_BACK.changeColor(self.posicion_del_mouse)
            self.PLAY_BACK.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.posicion_del_mouse):
                        pass

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

    def main_menu(self):
        while True:
            self.posicion_del_mouse = pg.mouse.get_pos()
            self.screen.blit(self.BG, (0, 0))
            print(self.posicion_del_mouse)
            self.MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            self.MENU_RECT = self.MENU_TEXT.get_rect(center = self.posicion_titulo)

            self.PLAY_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(self.x_centrada, 250), 
                                text_input="PLAY", font=self.get_font(75), base_color = self.color_boton, hovering_color = self.color_boton_al_apretar)
            self.LEVEL_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(self.x_centrada, 650), 
                                text_input="NIVELES", font=self.get_font(75), base_color = self.color_boton, hovering_color = self.color_boton_al_apretar)
            self.OPTIONS_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(self.x_centrada, 400), 
                                text_input="OPTIONS", font=self.get_font(75), base_color = self.color_boton, hovering_color = self.color_boton_al_apretar)
            self.QUIT_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(self.x_centrada, 550), 
                                text_input="QUIT", font=self.get_font(75), base_color = self.color_boton, hovering_color = self.color_boton_al_apretar)

            self.screen.blit(self.MENU_TEXT, self.MENU_RECT)

            for button in [self.PLAY_BUTTON, self.LEVEL_BUTTON,self.OPTIONS_BUTTON, self.QUIT_BUTTON]:
                button.changeColor(self.posicion_del_mouse)
                button.update(self.screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.LEVEL_BUTTON.checkForInput(self.posicion_del_mouse):
                        self.niveles()

                    if self.PLAY_BUTTON.checkForInput(self.posicion_del_mouse):

                        # self.game = GameManager()
                        # if self.game.loser == False:
                        #     self.game.run()
                        # elif self.game.loser == True:
                        #     self.menus = menu
                        #     self.menus.game_over()

                        self.game = GameManager()
                        self.game.run()


                    if self.OPTIONS_BUTTON.checkForInput(self.posicion_del_mouse):
                        # options()
                        self.pause()
                    if self.QUIT_BUTTON.checkForInput(self.posicion_del_mouse):
                        pg.quit()


            pg.display.update()
