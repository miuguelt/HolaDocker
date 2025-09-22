from flask import Flask
import os

app = Flask(__name__)

# Obtener el valor de la variable de entorno, si no existe, usar un valor por defecto
app_name = os.getenv('APP_NAME', 'Aplicación Flask')

@app.route('/')
def hola_mundo():
    return f'¡Hola Mundo con Flask desde {app_name}!'

@app.route('/index')
def hola_adso():
    return f'¡Hola - ADSO desde {app_name}!'

@app.route('/index2')
def hola_adso2():
    return f'¡Hola - ADSO2 desde {app_name}!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
