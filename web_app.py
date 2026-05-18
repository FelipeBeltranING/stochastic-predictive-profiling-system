from flask import Flask, render_template, request

from services.auth_service import authenticate

app = Flask(__name__, template_folder="ui/templates", static_folder="ui/static")


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/procesar', methods=['POST'])
def procesar_login():

    user = request.form.get('username')
    pas = request.form.get('password')
    resultado = authenticate(username=user, password=pas)
    

    if resultado["success"]:
        nombre_usuario = resultado["user"]["nombre"]
        perfil_usuario = resultado["user"]["perfil"]
        return f"<h1>¡{resultado['message']}!</h1><p>Bienvenido {nombre_usuario}, tu perfil es: {perfil_usuario}</p>"
    else:

        return f"<h1>Error de autenticación</h1><p>{resultado['message']}</p><a href='/'>Volver a intentar</a>"

if __name__ == '__main__':
    app.run(debug=True)