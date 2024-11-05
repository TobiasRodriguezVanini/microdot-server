from microdot import Microdot, send_file 
# Importo Microdot y la función send_file desde la libreria microdot

app = Microdot() 
# Se instancia Microdot

# Definimos la ruta raíz
@app.route('/')
async def index(request):
    return send_file('index.html')


@app.route('/<dir>/<file>') 
# Definimos la ruta 
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file) 
 # Nombre del archivo a enviar

# Prendemos el servidor en el puerto 80
app.run(port=80)
