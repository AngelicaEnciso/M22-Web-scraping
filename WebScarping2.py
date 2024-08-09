import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


# Configuración de opciones para el navegador

chrome_options = Options()

chrome_options.add_argument("--start-maximized")  # Abre el navegador en pantalla completa


# Configuración del controlador

service = Service(ChromeDriverManager().install())


# Inicializa el navegador

driver = webdriver.Chrome(service=service, options=chrome_options)


try:

    # Paso 1: Abre la página del Tec

    driver.get("https://itp.itpachuca.edu.mx/")


    # Espera a que el cuadro de búsqueda esté presente

    search_box = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.ID, "Ingenierias"))

    )

    search_box.send_keys("Ingenierías")

    search_box.submit()


    # Espera a que aparezcan los resultados

    pachuca_link = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Instituto Tecnológico de Pachuca"))

    )

    pachuca_link.click()


    # Espera a que la página del Instituto Tecnológico de Pachuca se cargue

    ingenierias_link = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.LINK_TEXT, "Ingenierias"))

    )

    ingenierias_link.click()


finally:

    # Mantén el navegador abierto

    input("Presiona Enter para cerrar el navegador...")

    driver.quit()