from funciones.utils import tomar_captura, correoGeneral
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException


def test_mayor_general_auto_suma(setup):
    archivo = "test_mayor_general_auto_suma"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "mayor_modulo").click()
    time.sleep(2)

    filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

    suma_calculada = 0.0

    for fila in filas:
        monto_texto = fila.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
        monto = float(monto_texto.replace(",", "").replace("€", "").strip())
        suma_calculada += monto

    auto_suma_texto = driver.find_element(By.CSS_SELECTOR, ".liqui_text.ayust").text
    auto_suma = float(auto_suma_texto.replace(",", "").replace("€", "").strip())

    assert (
        abs(suma_calculada - auto_suma) < 0.01
    ), f"Error: la suma calculada {suma_calculada} no coincide con la auto-suma {auto_suma}"

    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    tomar_captura(driver, f"completado {archivo}", archivo)
    print(
        f"Prueba completada. La suma de las transacciones es correcta: {suma_calculada}."
    )
    pass


def test_mayor_general_filtro_invalido(setup):
    archivo = "test_mayor_general_filtro_invalido"

    driver = setup
    time.sleep(3)

    correo_field = driver.find_element(By.ID, "correo")
    password_field = driver.find_element(By.ID, "clave")
    login_button = driver.find_element(By.CLASS_NAME, "btnx")

    correo_field.send_keys(correoGeneral)
    password_field.send_keys("1234")

    login_button.click()

    time.sleep(4)

    driver.find_element(By.ID, "mayor_modulo").click()
    time.sleep(2)
    tomar_captura(driver, "pagina" + "_" + archivo, archivo)

    try:
        driver.find_element(By.CLASS_NAME, "ayust1").send_keys("$$##$%")
        tomar_captura(driver, f"completado {archivo}", archivo)
        driver.find_element(By.CLASS_NAME, "search").click()
    except UnexpectedAlertPresentException:
        alert = Alert(driver)  # Captura la alerta
        alert_text = alert.text  # Lee el texto de la alerta

        time.sleep(2)
        print(
            f"Alerta inesperada: {alert_text}"
        )  # Muestra el texto de la alerta (opcional)
        alert.accept()  # Acepta la alerta para continuar
    print(f"completado {archivo}")
    pass
