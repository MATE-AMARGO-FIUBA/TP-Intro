import os
from flask import Flask, flash, jsonify, make_response, request, render_template, url_for, redirect, current_app
import smtplib
from email.mime.text import MIMEText
import requests
from blueprints.weatherAPI.weather import weatherBp
from blueprints.contacto.contacto import contactoBp
from blueprints.admin.admin import adminBp
from blueprints.index.index import indexBp
from blueprints.reservas.reserva import reservasBp
from blueprints.reviews.reviews import reviewsBp
from blueprints.nosotros.nosotros import nosotrosBp

app = Flask(__name__)
# Configurar la ruta de la API
app.config['API_ROUTE'] = 'http://127.0.0.1:5000/'

app.secret_key = os.urandom(24)
app.register_blueprint(weatherBp)
app.register_blueprint(contactoBp, url_prefix="/contacto")
app.register_blueprint(adminBp, url_prefix="/admin")
app.register_blueprint(indexBp, url_prefix='/')
app.register_blueprint(reservasBp, url_prefix="/reserva")
app.register_blueprint(reviewsBp, url_prefix="/reviews")
app.register_blueprint(nosotrosBp, url_prefix="/nosotros")


@app.route('/panel_admin', methods=["GET"])
def panel_admin():
    rol = request.cookies.get('rol')
    if rol == 'admin':
        return render_template('panel_administrador.html')
    
    return render_template('admin.html')

@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')

@app.route('/habitaciones/<id>', methods = ['GET'])
def habitaciones_id(id):
    return render_template('habitacion.html', id=id)

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/nosotros')
def sobre_nosotros():
    return render_template('nosotros.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)
