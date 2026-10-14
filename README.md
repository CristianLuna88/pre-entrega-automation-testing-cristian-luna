# Pre-Entrega: Automatización de Pruebas en SauceDemo

Este proyecto corresponde a la Pre-Entrega del curso de Automation Testing. Consiste en una suite de pruebas automatizadas sobre la plataforma web [SauceDemo](https://www.saucedemo.com/) utilizando **Python**, **Selenium WebDriver** y **Pytest**.

---

## Propósito del proyecto
El objetivo principal es validar de forma automatizada los flujos críticos de la aplicación web, garantizando la estabilidad de las funcionalidades clave:
1. **Autenticación (Login):** Validar el acceso con credenciales válidas y la correcta redirección a la vista de inventario con sincronización mediante esperas explícitas.
2. **Navegación y Catálogo:** Verificar la presencia y consistencia de los elementos estructurales de la interfaz de usuario, títulos de página, visualización de productos y obtención de datos dinámicos (nombre y precio).
3. **Interacción con Productos y Carrito:** Automatizar el flujo completo de compra (selección de un ítem, incremento del contador en el badge, navegación al carrito y verificación de persistencia del producto dentro del mismo).

---

##  Tecnologías utilizadas
* **Lenguaje:** [Python 3.12+](https://www.python.org/)
* **Framework de Pruebas:** [Pytest](https://docs.pytest.org/)
* **Automatización Web:** [Selenium WebDriver](https://www.selenium.dev/)
* **Gestor de Drivers:** [WebDriver Manager](https://pypi.org/project/webdriver-manager/) (manejo automático del binario de ChromeDriver)
* **Reportes:** [pytest-html](https://pypi.org/project/pytest-html/) (generación de informes visuales autosuficientes)
* **Control de versiones:** Git y GitHub

--- 

## 1 Clonar repositorio
* git clone https://github.com/CristianLuna88/pre-entrega-automation-testing-cristian-luna
* cd **pre-entrega-automation-testing-cristian-luna**

## (Opcional) Crear y activar un entorno virtual:
* python -m venv venv
* source venv/Scripts/activate

## Instalar los paquetes requeridos:
* pip install pytest pytest-html selenium webdriver-manager

---

# Cómo ejecutar las pruebas
Asegurate de estar ubicado en la raíz del proyecto para ejecutar los comandos.

## 1. Ejecución con generación de reporte HTML (Comando de entrega)
Ejecuta la suite de pruebas detallando cada caso en consola (-v) y genera el archivo reporte.html autosuficiente dentro de la carpeta reports/:
* pytest test/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html

## 2. Ejecución con reporte HTML y visualización de salidas por consola (print)
Incluye la opción -s para desactivar la captura de salidas estándar y ver los mensajes en la terminal:
* pytest test/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html

## 3. Ejecución directa en terminal (sin generar reporte HTML)
* pytest test/test_saucedemo.py -v -s

## 4. Ejecutar un caso de prueba individual
Podés ejecutar un test específico indicando su nombre con -k:
* pytest test/test_saucedemo.py -v -s -k "test_07_verificar_añadir_producto_al_carrito"
