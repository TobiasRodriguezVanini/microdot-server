# Aplicacion del servidor
from microdot import Microdot, send_file # Importamos la clase Microdot y la función send_file
from machine import Pin, PWM 
# Importo la clase Microdot, Pin y PWE. Tambien la funcion send_file.
import time


app = Microdot() 
# Instanciamos Microdot

LED1 = Pin(32, Pin.OUT) 
LED2 = Pin(33, Pin.OUT) 
LED3 = Pin(25, Pin.OUT) 
# Defino los pines 32,33,25 como salida

@app.route('/')
async def index(request):
    return send_file('index.html')
# Definimos la ruta raíz

@app.route('/<dir>/<file>') 
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file)
# Definimos la ruta y cambiamos le nombre del archivo a enviar. 



@app.route('/toggle/led/<int:id>') 
# Definimos la ruta con el parámetro entero
async def index(request, id):

    # Dependiendo del valor del parámetro id, encendemos o apagamos un LED
    if id == 1:
        LED1.value(not LED1.value())

    elif id == 2:
        LED2.value(not LED2.value())

    elif id == 3:
        LED3.value(not LED3.value())

    return 'OK'

# Corremos el servidor en el puerto 80
app.run(port=80)