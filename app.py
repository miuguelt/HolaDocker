from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo con Flask!'

@app.route('/index')
def hola_adso():
    return '¡Hola - ADSO!'

@app.route('/index2')
def hola_adso2():
    return '¡Hola - ADSO2!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 