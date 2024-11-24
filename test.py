from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


from funciones.registro import test_registro, test_registro_correo_invalido

from funciones.login import test_login_correcto, test_login_incorrecto

from funciones.registro_cliente import (
    test_registro_cliente,
    test_registro_cliente_duplicado,
)

from funciones.registro_transacciones import (
    test_registro_transacciones,
    test_registro_transacciones_invalida,
)
from funciones.mayor_general import (
    test_mayor_general_auto_suma,
    test_mayor_general_filtro_invalido,
)


@pytest.fixture
def setup():
    options = Options()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get("https://appcontable.netlify.app/log")
    yield driver
    driver.quit()
