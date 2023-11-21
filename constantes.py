import json

PATH_IMAGE = "/CLASE_19_inicio_juego/images/"

def cargar_settings(ruta_del_archivo_json) -> dict:

    with open(ruta_del_archivo_json,"r") as file:
        return json.load(file)
    

settings = cargar_settings("config/settings.json").get("configuraciones_generales")

ANCHO_VENTANA = settings.get("ANCHO_VENTANA")
ALTO_VENTANA = settings.get("ALTO_VENTANA")
FPS = settings.get("FPS")

niveles = cargar_settings("config/settings.json").get("niveles")

