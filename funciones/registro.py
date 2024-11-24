from funciones.utils import tomar_captura, correoGeneral
import time
from selenium.webdriver.common.by import By


def test_registro(setup):
    archivo = "test_registro"
    driver = setup
    time.sleep(3)
    enlace = driver.find_element(By.ID, "register-link")
    enlace.click()
    time.sleep(2)

    nombre_field = driver.find_element(By.ID, "Nombre")
    correo_field = driver.find_element(By.ID, "Correo")
    clave_field = driver.find_element(By.ID, "Clave")
    repetir_clave_field = driver.find_element(By.ID, "RepetirClave")
    registro_button = driver.find_element(By.ID, "boton-registro")

    nombre_field.send_keys("Juan Pérez")
    correo_field.send_keys(correoGeneral)
    clave_field.send_keys("1234")
    repetir_clave_field.send_keys("1234")

    registro_button.click()

    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    time.sleep(3)

    # boton del login
    driver.find_element(By.CLASS_NAME, "btnx")
    tomar_captura(driver, archivo, archivo)
    print(f"completado {archivo}")
    pass


def test_registro_correo_invalido(setup):
    archivo = "test_registro_correo_invalido"
    driver = setup
    time.sleep(3)
    enlace = driver.find_element(By.ID, "register-link")
    enlace.click()
    time.sleep(2)

    nombre_field = driver.find_element(By.ID, "Nombre")
    correo_field = driver.find_element(By.ID, "Correo")
    clave_field = driver.find_element(By.ID, "Clave")
    repetir_clave_field = driver.find_element(By.ID, "RepetirClave")
    registro_button = driver.find_element(By.ID, "boton-registro")

    nombre_field.send_keys("Juan Pérez")
    correo_field.send_keys("juanperez.com")
    clave_field.send_keys("password123")
    repetir_clave_field.send_keys("password123")

    registro_button.click()

    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    time.sleep(3)

    # boton del login
    driver.find_element(By.XPATH, "//p[text()='El Correo no es valido']")
    tomar_captura(driver, archivo, archivo)
    print(f"completado {archivo}")
    pass
