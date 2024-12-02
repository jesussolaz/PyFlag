# PyFlag
Aplicación en Python diseñada para revisar y analizar un archivo Excel que contiene las siguientes columnas: Mes, Llamadas, Clientes Satisfechos, Ventas y Empleados Trabajando. Además, genera gráficas a partir de los datos y resalta variaciones inusuales para facilitar su interpretación.

# Instalación PyFlag:
1.- Instalar Python desde la Microsoft Store.

2.- Descarga el archivo get-pip.py desde [aquí](https://bootstrap.pypa.io/get-pip.py). Luego, en una terminal, navega a la ubicación del archivo y ejecuta el siguiente código para instalar pip:

``` Terminal Windows
python get-pip.py
```
3.- Instalar dependencias ejecutando el siguiente comando:
``` Terminal Windows
pip install streamlit pandas matplotlib
```
# Ejecución PyFlag:
Una vez instaladas todas las dependencias necesarias para el programa, podemos proceder a inicializarlo:

1.- Navega al directorio donde está guardado el archivo app.py y ejecuta el siguiente comando:

```
streamlit run pyflag.py
```
2.- El comando anterior abrirá la aplicación de PyFlag en el navegador. No obstante, si no ocurre automáticamente, copia y pega la URL que aparece en la terminal, como por ejemplo http://localhost:8501.
