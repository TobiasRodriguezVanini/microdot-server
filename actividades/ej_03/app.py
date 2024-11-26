# Aplicacion del servidor
from boot import do_connect
from microdot import Microdot, send_file # Importamos la clase Microdot y la función send_file
from machine import Pin, PWM, ADC # Importamos las clases Pin y PWM
import time
import ds18x20
import onewire


app = Microdot() # Instanciamos la clase Microdot


LED1 = Pin(32, Pin.OUT) # Definimos el pin 32 como salida
LED2 = Pin(33, Pin.OUT) # Definimos el pin 33 como salida
LED3 = Pin(25, Pin.OUT) # Definimos el pin 25 como salida
buzzer_pin = Pin(14, Pin.OUT) # Definimos el pin 26 como salida
ds_pin = Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
temperaturaCelsius = 24

do_connect() # Conectamos el ESP32 a la red WiFi


# Definimos la ruta raíz
@app.route('/')
async def index(request):
    return send_file('index.html')




@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))



@app.route('/toggle/led/<int:id>') # Definimos la ruta con un parámetro entero
async def index(request, id):

    # Dependiendo del valor del parámetro id, encendemos o apagamos un LED
    if id == 1:
        LED1.value(not LED1.value())

    elif id == 2:
        LED2.value(not LED2.value())

    elif id == 3:
        LED3.value(not LED3.value())

    return 'OK'

@app.route('/sensors/ds18b20/read')
async def temperature_measuring(request):
    global ds_sensor
    ds_sensor.convert_temp()
    time.sleep_ms(1)
    roms = ds_sensor.scan()
    for rom in roms:
        temperatureCelsius = ds_sensor.read_temp(rom)
    
    json = {'temperature': temperatureCelsius};
    
    return json

@app.route('/setpoint/set/<int:value>')
async def setpoint_calculation(request, value):
    json = {}
    print("Calculate setpoint")
    if value >= temperatureCelsius:
        buzzer_pin.on()
        json = {'buzzer': 'On'}
    else:
        buzzer_pin.off()
        json = {'buzzer': 'Off'}
    
    return json 

# Corremos el servidor creado en el puerto 80
app.run(port=80)