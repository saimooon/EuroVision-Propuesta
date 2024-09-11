from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'simon.andaurt@gmail.com'
app.config['MAIL_PASSWORD'] = 'nvvz bser uqrc tbht'
app.config['MAIL_DEFAULT_SENDER'] = 'simon.andaurt@gmail.com'  # Remitente por defecto (debe ser tu Gmail)

mail = Mail(app)
app.secret_key = '770Nj+3nSH|g'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/participantes', methods=['GET', 'POST'])
def participantes():
    if request.method == 'POST':
        # Captura los datos del formulario
        nombre = request.form['name']
        email = request.form['email']
        link = request.form.get('link', 'No proporcionado')  # El campo link puede ser opcional
        mensaje = request.form['message']

        # Crear el mensaje de correo con asunto
        msg = Message('Sugerencia de participante',  # Asunto del correo
                      sender=app.config['MAIL_DEFAULT_SENDER'],  # Usa el remitente por defecto
                      recipients=['simon.andaurt@gmail.com'])  # Destinatario
        msg.body = f"Nombre: {nombre}\nCorreo: {email}\nLink: {link}\nMensaje:\n{mensaje}"

        try:
            # Enviar el correo
            mail.send(msg)
            flash('Formulario enviado correctamente!', 'success')  # Flash message de éxito
        except Exception as e:
            flash(f'Ocurrió un error al enviar el formulario: {e}', 'danger')  # Flash message de error

        return redirect('/participantes')

    return render_template('participantes.html', participantes=participantes_info)

@app.route('/canciones', methods=['GET', 'POST'])
def canciones():
    # Lista de videos de canciones de Eurovisión
    videos = [
        {
            "url": "https://www.youtube.com/embed/L_dWvTCdDQ4",
            "title": "Little Big - Uno - Russia 🇷🇺 - Official Music Video - Eurovision 2020",
            "description": "Little Big represented Russia at the Eurovision Song Contest 2020 in Rotterdam with the song Uno.",
            "country": "Russia 🇷🇺"
        },
        {
            "url": "https://www.youtube.com/embed/CziHrYYSyPc",
            "title": "Netta - TOY - Israel - Official Music Video - Eurovision 2018",
            "description": "Netta represented Israel at the 2018 Eurovision Song Contest in Lisbon with the song TOY.",
            "country": "Israel 🇮🇱"
        },
        {
            "url": "https://www.youtube.com/embed/RVH5dn1cxAQ",
            "title": "Måneskin - Zitti E Buoni - Italy 🇮🇹 - Grand Final - Eurovision 2021",
            "description": "Måneskin represented Italy at the Grand Final of the Eurovision Song Contest 2021 with the song Zitti E Buoni.",
            "country": "Italy 🇮🇹"
        },
        {
            "url": "https://www.youtube.com/embed/WXwgZL4zx9o",
            "title": "Alexander Rybak - Fairytale - LIVE | Norway 🇳🇴 | Grand Final | Eurovision 2009",
            "description": "Alexander Rybak represented Norway in the 2009 Eurovision Song Contest with the song 'Fairytale'. Norway won the grand final and brought the Eurovision Song Contest to Oslo in 2010.",
            "country": "Norway 🇳🇴"
        },
    ]

    if request.method == 'POST':
        # Capturar los datos del formulario
        email = request.form['email']
        link = request.form['link']
        message = request.form.get('message', 'No se proporcionó mensaje')  # El mensaje es opcional

        # Crear el mensaje de correo
        msg = Message('Sugerencia de canción',  # Asunto del correo
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=['simon.andaurt@gmail.com'])  # Cambia al correo del destinatario
        msg.body = f"Correo: {email}\nLink a la canción: {link}\nMensaje: {message}"

        try:
            # Intentar enviar el correo
            mail.send(msg)
            flash('Formulario enviado correctamente. ¡Gracias por tu sugerencia!', 'success')  # Mensaje de éxito
        except Exception as e:
            flash(f'Ocurrió un error al enviar el formulario: {e}', 'danger')  # Mensaje de error si falla

        return redirect('/canciones')  # Redirigir a la misma página después de enviar

    return render_template('canciones.html', videos=videos)


@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')



@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    if request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        mensaje = request.form['message']

        # Crear el mensaje de correo
        msg = Message('Nuevo mensaje de contacto', 
                      sender=app.config['MAIL_DEFAULT_SENDER'],  # Usa el remitente por defecto
                      recipients=['simon.andaurt@gmail.com'])  # Destinatario
        msg.body = f"Nombre: {nombre}\nCorreo: {email}\nMensaje:\n{mensaje}"

        try:
            # Enviar el correo
            mail.send(msg)
            flash('Mensaje enviado correctamente!', 'success')  # Flash message de éxito
        except Exception as e:
            flash(f'Ocurrió un error: {e}', 'danger')  # Flash message de error

        return redirect('/contactos')

    return render_template('contactos.html')


@app.route('/ganadores')
def ganadores():
    videos = [
        {
            "url": "https://www.youtube.com/embed/BE2Fj0W4jP4",
            "title": "Loreen - 'Tattoo' (583 puntos)",
            "description": "Loreen ha ganado Eurovisión 2023 con 583 puntos...",
            "year": 2023
        },
        {
            "url": "https://www.youtube.com/embed/F1fl60ypdLs?si=AOC0PXKnRO5f0W9Q",
            "title": "Kalush Orchestra - Stefania (631 puntos)",
            "description": "La Orquesta Kalush de Ucrania ganó el Festival de Eurovisión 2022...",
            "year": 2022
        },
        {
            "url": "https://www.youtube.com/embed/9mL6Cmkg2_A?si=9EojP3u4PN2VpfFe",
            "title": "Måneskin - Zitti E Buoni",
            "description": "Måneskin representará a Italia en el Festival de la Canción de Eurovisión 2021...",
            "year": 2021
        },
        {
            "url": "https://www.youtube.com/embed/R3D-r4ogr7s?si=l4RpOuH1294wH5C-",
            "title": "Duncan Laurence - Arcade",
            "description": "Duncan Laurence representó a los Países Bajos en Eurovisión 2019...",
            "year": 2019
        },
        {
            "url": "https://www.youtube.com/embed/84LBjXaeKk4?si=25aZGTgyxAOW1hhr",
            "title": "Netta - Toy",
            "description": "Netta representó a Israel en la Gran Final del Festival de la Canción de Eurovisión 2018...",
            "year": 2018
        }
    ]
    return render_template('ganadores.html', videos=videos)



# Nueva ruta para la votación
@app.route('/votacion', methods=['GET', 'POST'])
def votacion():
    if request.method == 'POST':
        # Obtener el ID del participante seleccionado
        participante_id = int(request.form['participante'])
        # Incrementar los votos del participante correspondiente
        for participante in participantes_info:
            if participante['id'] == participante_id:
                participante['votes'] += 1
                break
        return redirect(url_for('votacion'))

    # Mostrar la página de votación con los participantes y sus votos
    return render_template('votacion.html', participantes=participantes_info)

participantes_info = [
    {
        "id": 1,
        "name": "BESA - TITAN ",
        "country": "Albania 🇦🇱",
        "song": "BESA - TITAN ",
        "description": "BESA representará a Albania en el Festival de Eurovisión con su canción TITAN.",
        "video_url": "https://www.youtube.com/embed/nrjFhjpm7D8?si=zn6kJ1mD_-VYlpc9"  # O URL de YouTube
    },
    {
        "id": 2,
        "name": "Nutsa Buzaladze - Firefighter",
        "country": "Georgia 🇬🇪",
        "song": "Nutsa Buzaladze - Firefighter",
        "description": "Nutsa Buzaladze representará a Georgia en el Festival de Eurovisión con su canción Firefighter.",
        "video_url": "https://www.youtube.com/embed/blMwY8Jabyk?si=jd8gBvRr1yjzKNdX"
    },
    {
        "id": 3,
        "name": "Bambie Thug - Doomsday Blue",
        "country": "Ireland 🇮🇪",
        "song": "Bambie Thug - Doomsday Blue",
        "description": "Bambie Thug representará a Irlanda en el Festival de Eurovisión con la canción Doomsday Blue.",
        "video_url": "https://www.youtube.com/embed/ZGRXRrlIspY?si=sUt_rsHw-cpfQUD-"
    },
    {
        "id": 4,
        "name": "Nebulossa - ZORRA",
        "country": "Spain 🇪🇸",
        "song": "Nebulossa - ZORRA",
        "description": "Nebulossa representará a España en el Festival de Eurovisión 2024 con su canción Zorra.",
        "video_url": "https://www.youtube.com/embed/LJFpexlj9Bs?si=_tx2Xh6S1g2ARiRQ"
    }
]




if __name__ == '__main__':
    app.run(debug=True)
