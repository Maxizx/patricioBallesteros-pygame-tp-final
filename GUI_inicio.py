import pygame as pg
from constantes import (ANCHO_VENTANA,ALTO_VENTANA)
from botones import Button as Button
from game import GameManager
# from main import game

# if __name__ == "__main__":

pg.init()

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.display.set_caption("Menu")

BG = pg.image.load("images/locations/fondos/Purple.png")
BG = pg.transform.scale(BG, (ANCHO_VENTANA, ALTO_VENTANA))

rescalado = (800,400)
panel_menu_niveles = pg.image.load("images/UI/PNG/blue_panel.png")
panel_menu_niveles = pg.transform.scale(panel_menu_niveles,(rescalado))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("images/UI/Font/kenvector_future_thin.ttf", size)

x_centrada= ANCHO_VENTANA/2
posicion_titulo = (x_centrada,100)
posicion_centrada = (x_centrada, ALTO_VENTANA/2)
posicion_centrada_abajo = (x_centrada, (ALTO_VENTANA/2)+100)
color_boton = "Black"
color_boton_al_apretar = "White"
color_letras = "Black"

def game_over():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        screen.fill("black")

        PLAY_TEXT = get_font(70).render("Gave Over", True, (255,45,0))
        PLAY_RECT = PLAY_TEXT.get_rect(center= posicion_centrada)
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos= posicion_centrada_abajo, 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()

def pause():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        screen.fill("black")

        boton_subir = pg.image.load("images/UI/PNG/grey_arrowUpWhite.png")
        boton_subir_rect = boton_subir.get_rect(center= ((x_centrada)-50,300))
        boton_bajar = pg.image.load("images/UI/PNG/grey_arrowDownWhite.png")
        boton_bajar_rect = boton_bajar.get_rect(center= (x_centrada,300))


        PLAY_TEXT = get_font(45).render("Pause", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center= (x_centrada,200))
        screen.blit(boton_subir, boton_subir_rect)
        screen.blit(boton_bajar, boton_bajar_rect)

        PLAY_TEXT = get_font(45).render("Pause", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center= (x_centrada,200))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=posicion_centrada_abajo, 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()
    
def niveles():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        print(PLAY_MOUSE_POS)
        screen.fill("black")

        PLAY_TEXT = get_font(45).render("Selecciona tu nivel.", True, color_boton_al_apretar)
        PLAY_RECT = PLAY_TEXT.get_rect(center= posicion_titulo)
        screen.blit(PLAY_TEXT, PLAY_RECT)
        screen.blit(panel_menu_niveles,(250, 160))

        PLAY_BACK = Button(image="images/UI/PNG/grey_button02.png", pos=(640,630), text_input="BACK", font=get_font(75), base_color=color_letras, hovering_color="Green")
        level_one = Button(image="images/UI/PNG/grey_button02.png", pos=(x_centrada,250), text_input=" LEVEL 1 ", font=get_font(75), base_color = color_letras, hovering_color="Green")
        level_two = Button(image="images/UI/PNG/grey_button02.png", pos=(x_centrada,350), text_input=" LEVEL 2 ", font=get_font(75), base_color = color_letras, hovering_color="Green")
        level_three = Button(image="images/UI/PNG/grey_button02.png", pos=(x_centrada,450), text_input=" LEVEL 3 ", font=get_font(75), base_color =  color_letras, hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        level_one.changeColor(PLAY_MOUSE_POS)
        level_two.changeColor(PLAY_MOUSE_POS)
        level_three.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        level_one.update(screen)
        level_two.update(screen)
        level_three.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pass

        pg.display.update()
    
def play():
    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()
        screen.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center= posicion_centrada)
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=posicion_centrada_abajo, text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pass

        pg.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center= posicion_centrada)
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=posicion_centrada_abajo, 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update()

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()



        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center = posicion_titulo)

        PLAY_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(x_centrada, 250), 
                            text_input="PLAY", font=get_font(75), base_color = color_boton, hovering_color = color_boton_al_apretar)
        LEVEL_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(x_centrada, 650), 
                            text_input="NIVELES", font=get_font(75), base_color = color_boton, hovering_color = color_boton_al_apretar)
        OPTIONS_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(x_centrada, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color = color_boton, hovering_color = color_boton_al_apretar)
        QUIT_BUTTON = Button(image="images/UI/PNG/blue_button04.png", pos=(x_centrada, 550), 
                            text_input="QUIT", font=get_font(75), base_color = color_boton, hovering_color = color_boton_al_apretar)

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LEVEL_BUTTON,OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    niveles()

                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game = GameManager()
                    game.run()

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # options()
                    pause()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()


        pg.display.update()

main_menu()