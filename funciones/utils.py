from datetime import datetime
import os

# este va ser el correo general para los test siempre se tiene que cambiar por uno nuevo
correoGeneral = "henryfuerte5679@gmail.com"


def tomar_captura(driver, nombre_archivo, subcarpeta):
    carpeta_completa = os.path.join("assets", subcarpeta)

    if not os.path.exists(carpeta_completa):
        os.makedirs(carpeta_completa)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo_completo = f"{nombre_archivo}_{timestamp}.png"

    filepath = os.path.join(carpeta_completa, nombre_archivo_completo)

    driver.save_screenshot(filepath)
