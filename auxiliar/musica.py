import pygame as pg
from auxiliar.constantes import cargar_settings

configuraciones = cargar_settings("config/settings.json").get("configuraciones_generales")
path_musica = configuraciones.get("FOLDER_MUSIC")
volumen_default = configuraciones.get("VOLUMEN_DEFAULT")


class audio:
    def __init__(self,nombre, volumen, repetir = 0, ubi = path_musica) -> None:
        self.nombre_de_la_cancion = nombre
        self.volumen_del_audio = volumen
        self.mixer_audio= pg.mixer.Sound(f"{ubi}/{self.nombre_de_la_cancion}.mp3") 
        self.repetir = repetir

    def reproducir_audio(self):
        self.mixer_audio.set_volume(self.volumen_del_audio)
        self.mixer_audio.play(self.repetir)

    def mutear_sonido(self):
        self. mixer_audio.set_volume(0)
    
    def get_volumen_del_audio(self):
        return self.mixer_audio.get_volume() 

    def control_volumen(self, aumentar = True):
        if self.mixer_audio.get_volume() < 0.1 and self.mixer_audio.get_volume() > 0.0:
            if aumentar == True:
                self.volumen_del_audio += 0.01
            elif aumentar == False:
                self.volumen_del_audio -= 0.01
            elif self.mixer_audio.get_volume() == 0.0 and aumentar == True:
                self.volumen_del_audio += 0.01
            elif aumentar == False and self.mixer_audio.get_volume() == 0.1:
                self.volumen_del_audio -= 0.01
        else:
            print("El audio está muy alto o está muteado")





