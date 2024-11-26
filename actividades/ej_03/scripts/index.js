function leer_temperatura() {
    fetch('/sensors/ds18b20/read')
        .then(response => response.json())
        .then(json => {
            document.querySelector('#temperatura').innerText = json.temperature;
        })
        .catch(error => console.error('Error al leer la temperatura:', error));
}

function enviar_temperatura() {
    let temperature_slider_value = parseInt(document.querySelector('#temperature-slider').value);
    fetch(`/setpoint/set/${temperature_slider_value}`)
        .then(response => response.json())
        .then(json => {
            document.querySelector('#buzzer-state').innerText = json.buzzer;
        })
        .catch(error => console.error('Error al enviar la temperatura:', error));
}

function updateTemperatura(value) {
    document.getElementById('temperature_slider_value').innerText = value;
    enviar_temperatura();
}

// Actualiza la temperatura cada 500ms
setInterval(leer_temperatura, 500);
