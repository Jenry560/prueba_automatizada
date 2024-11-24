from funciones.utils import tomar_captura, correoGeneral
import time
from selenium.webdriver.common.by import By


# Función de prueba para login correcto
def test_registro_cliente(setup):
    archivo = "test_registro_cliente"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "cliente_modulo").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "icon_add").click()
    time.sleep(2)

    codigoIngresa = "12345"
    codigo_field = driver.find_element(By.ID, "Codigo")
    codigo_field.send_keys(codigoIngresa)

    nombre_field = driver.find_element(By.ID, "Nombre")
    nombre_field.send_keys("Juan Perez")

    direccion_field = driver.find_element(By.ID, "Direccion")
    direccion_field.send_keys("Calle Principal #123")

    numero_field = driver.find_element(By.ID, "Numero")
    numero_field.send_keys("8091234567")

    cedula_field = driver.find_element(By.ID, "Cedula")
    cedula_field.send_keys("00112345678")
    submit_button = driver.find_element(By.ID, "btn-registro")
    submit_button.click()
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    time.sleep(4)
    driver.find_element(
        By.XPATH, "//td[@class='value']/a[text()='" + codigoIngresa + "']"
    )
    tomar_captura(driver, f"completado {archivo}", archivo)

    print(f"completado {archivo}")
    pass


# Función de prueba para login incorrecto
def test_registro_cliente_duplicado(setup):
    archivo = "test_registro_cliente_duplicado"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "cliente_modulo").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "icon_add").click()
    time.sleep(2)

    # codigo duplicado
    codigoIngresa = "12345"
    codigo_field = driver.find_element(By.ID, "Codigo")
    codigo_field.send_keys(codigoIngresa)

    nombre_field = driver.find_element(By.ID, "Nombre")
    nombre_field.send_keys("Juan Perez")

    direccion_field = driver.find_element(By.ID, "Direccion")
    direccion_field.send_keys("Calle Principal #123")

    numero_field = driver.find_element(By.ID, "Numero")
    numero_field.send_keys("8091234567")

    cedula_field = driver.find_element(By.ID, "Cedula")
    cedula_field.send_keys("00112345678")
    submit_button = driver.find_element(By.ID, "btn-registro")
    submit_button.click()
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    time.sleep(2)
    driver.find_element(By.ID, "repetido")

    tomar_captura(driver, f"completado {archivo}", archivo)

    print(f"completado {archivo}")
    pass
