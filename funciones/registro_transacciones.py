from funciones.utils import tomar_captura, correoGeneral
import time
from selenium.webdriver.common.by import By


# Función de prueba para login correcto
def test_registro_transacciones(setup):
    archivo = "test_registro_transacciones"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "registro_modulo").click()
    time.sleep(2)

    codigo_field = driver.find_element(By.ID, "Codigo")
    asiento_field = driver.find_element(By.ID, "Asiento")
    descripcion_field = driver.find_element(By.ID, "Descripcion")
    partida_field = driver.find_element(By.ID, "Partida")
    monto_field = driver.find_element(By.ID, "Monto")
    submit_button = driver.find_element(By.ID, "Submit")

    codigo_field.send_keys("7080")
    asiento_field.send_keys("PG")
    descripcion_field.send_keys("Descripción de prueba")
    partida_field.send_keys("Debito")
    monto_field.send_keys("1000")
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    submit_button.click()

    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "cambio2")
    tomar_captura(driver, f"completado {archivo}", archivo)

    print(f"completado {archivo}")
    pass


# Función de prueba para login incorrecto
def test_registro_transacciones_invalida(setup):
    archivo = "test_registro_transacciones_invalida"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "registro_modulo").click()
    time.sleep(2)

    codigo_field = driver.find_element(By.ID, "Codigo")
    asiento_field = driver.find_element(By.ID, "Asiento")
    descripcion_field = driver.find_element(By.ID, "Descripcion")
    partida_field = driver.find_element(By.ID, "Partida")
    monto_field = driver.find_element(By.ID, "Monto")
    submit_button = driver.find_element(By.ID, "Submit")

    codigo_field.send_keys("5555")
    asiento_field.send_keys("PG")
    descripcion_field.send_keys("Descripción de prueba")
    partida_field.send_keys("Debito")
    monto_field.send_keys("1000")
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    submit_button.click()

    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "cambio1")
    tomar_captura(driver, f"completado {archivo}", archivo)

    print(f"completado {archivo}")
    pass
