from funciones.utils import tomar_captura, correoGeneral
import time
from selenium.webdriver.common.by import By


# Función de prueba para login correcto
def test_login_correcto(setup):
    archivo = "test_login_correcto"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    login_button.click()

    time.sleep(4)

    driver.find_element(By.CLASS_NAME, "navbal")
    tomar_captura(driver, archivo, archivo)
    print(f"completado {archivo}")
    pass


# Función de prueba para login incorrecto
def test_login_incorrecto(setup):
    archivo = "test_login_incorrecto"
    driver = setup
    time.sleep(3)
    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")
    correo_field.send_keys("incorrecto@gmail.com")
    password_field.send_keys("wrongpassword")
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)
    login_button.click()
    time.sleep(2)
    driver.find_element(By.ID, "error-message")  # Cambia este selector según el caso
    tomar_captura(driver, archivo, archivo)
    print(f"completado {archivo}")
    pass
