import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

#separar
@pytest.fixture()
def driver():
    service= Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)
    
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
    
def test_01_login(driver):
    login(driver)
    
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url , "ERROR: No se ha podido redirigir a inventory.html"

def test_02_verificacion_de_titulo_de_pagina(driver):
    login(driver)
    titulo_de_pagina= driver.title

    assert titulo_de_pagina == "Swag Labs" , f'ERROR: Titulo de ventana esperado "Swag Labs", titulo obtenido {titulo_de_pagina}'

    
def test_03_verificar_titulo_de_seccion(driver):
    login(driver)
    titulo_seccion = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_seccion == "Products", f"ERROR: El titulo de seccion esperado es 'Products' es {titulo_seccion}"

def test_04_productos_visibles(driver):
    login(driver)
    productos= driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0 , "ERROR: No se encontrarron productos en la pagina"
    print(f"Se encontraron {len(productos)} productos en el catálogo")

def test_05_verificar_elementos_importantes(driver):
    login(driver)
    elementos_importantes= [
        (By.ID, "react-burger-menu-btn"),
        (By.CLASS_NAME, "app_logo"),
        (By.CLASS_NAME, "shopping_cart_link"),
        (By.CLASS_NAME, "inventory_list"),
        (By.CLASS_NAME, "product_sort_container"),
        (By.CLASS_NAME, "footer"),
        (By.CLASS_NAME, "social"),
        (By.CLASS_NAME, "footer_copy")
    ]
    for elemento in elementos_importantes:
        assert driver.find_element(*elemento).is_displayed(), f"ERROR: El elemento {elemento} no se ve"

def test_06_nombre_y_precio_primer_producto(driver):
    login(driver)
    productos= driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    precios= driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    nombre_primer_producto= productos[0].text
    precio_primer_producto= precios[0].text

    print(f"El nombre y precio del primer producto es: {nombre_primer_producto} {precio_primer_producto}")
    assert nombre_primer_producto != "", "ERROR: El nombre del producto está vacío"
    assert "$" in precio_primer_producto, "ERROR: El precio no tiene un formato válido"
    
    
def test_07_verificar_añadir_producto_al_carrito(driver):
    login(driver)
    #agrego el primer producto al carrito
    primer_producto= driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    agregar_al_carrito= primer_producto.find_element(By.TAG_NAME, "button")
    agregar_al_carrito.click()
    
    #verifico que el contador subio a 1
    carrito = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")) )
    
    assert carrito.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {carrito.text}"
    print("Producto añadido al carrito correctamente!")

    #voy al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    #compruebo que el producto esta en el carrito
    producto_en_carrito= WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CLASS_NAME,"cart_item")))
    
    assert producto_en_carrito.is_displayed(), "ERROR: El producto no esta en el carrito"