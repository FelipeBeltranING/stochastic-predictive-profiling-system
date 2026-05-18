from flask import Flask, render_template, request, redirect, url_for, session
from services.auth_service import authenticate
from services.search_service import search_products
from services.ad_service import get_prioritized_ads
from database.data_store import usuarios, update_user_profile

app = Flask(__name__, template_folder="ui/templates", static_folder="ui/static")
app.secret_key = 'stochastic_profiling_lab_2024'


@app.route('/')
def login_page():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    result = authenticate(username=username, password=password)

    if result["success"]:
        session['username'] = username.lower()
        session['nombre'] = result["user"]["nombre"]
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error=result["message"])


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login_page'))

    username = session['username']
    user_data = usuarios[username]
    perfil = user_data["perfil"]

    # Publicidad ordenada por cola de prioridad
    ads = get_prioritized_ads(perfil, top_n=5)

    # Perfil ordenado por nivel de interés
    sorted_profile = sorted(perfil.items(), key=lambda x: x[1], reverse=True)

    return render_template('dashboard.html',
                           nombre=session['nombre'],
                           perfil=sorted_profile,
                           ads=ads)


@app.route('/search')
def search():
    if 'username' not in session:
        return redirect(url_for('login_page'))

    query = request.args.get('q', '')
    username = session['username']
    user_data = usuarios[username]
    perfil = user_data["perfil"]

    results, search_tags = search_products(query, perfil)

    # Actualizar perfil del usuario según búsqueda
    if search_tags:
        update_user_profile(username, search_tags)

    # Publicidad para sidebar
    ads = get_prioritized_ads(perfil, top_n=3)

    # Perfil actualizado
    sorted_profile = sorted(
        usuarios[username]["perfil"].items(),
        key=lambda x: x[1], reverse=True
    )

    return render_template('results.html',
                           nombre=session['nombre'],
                           query=query,
                           results=results,
                           ads=ads,
                           perfil=sorted_profile)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == '__main__':
    app.run(debug=True)