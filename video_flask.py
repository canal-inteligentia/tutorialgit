from flask import Flask, render_template
from videos import video_class

app = Flask(__name__)

@app.route('/')
def hello_world():
    apartamento = video_class.apartamento_1

    mensaje = f"El apartamento en el piso {apartamento.piso} con orientacion {apartamento.orientacion} cuesta {apartamento.precio}"

    return render_template('index.html', mensaje = mensaje)

if __name__ == '__main__':
    app.run()