""" Tarea Programa 4,
	Realizado por:  Andres Fernadez,
					Luigui Madrigal,
					Jose Maria Rojas"""

import os, backend
from flask import Flask, render_template, request, redirect, url_for, make_response
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic

from config import CONFIG

app = Flask("Apts")#instancia de la aplicacion web con Flask
app.debug = True#debugger de la app

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'BuscaApartaTec', report_errors=False)

#pagina inicial
@app.route('/')
def home():
	return render_template('index.html')
	
#pagina para buscar apartamentos
@app.route('/buscar')
def buscar():
	return render_template('buscar.html')
	
#pagina para mostrar resultado de la busqueda
@app.route('/resultado', methods=['POST'])
def resultado():
	facilidades = request.form.getlist('facilidad')#lista con las facilidades
	habitaciones = request.form['habitaciones']
	banos = request.form['banos']
	estacionamientos = request.form['estacionamientos']
	precio_inicial = request.form['precio_inicial']
	precio_final = request.form['precio_final']
	#lista = backend.leer()
	lista= backend.filtrar(facilidades, habitaciones, banos, estacionamientos, precio_inicial, precio_final)#lista de objetos publicacion
	return render_template('mostrar.html', lista = lista)
	
#ruta para login de facebook
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    """}
Login handler, must accept both GET and POST to be able to use OpenID.
"""
    
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
    
    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
        
        # The rest happens inside the template.
        
        return render_template('layout.html', result=result)
    
    # Don't forget to return the response.
    return response
    

#pagina para agregar apartamentos
@app.route('/publicar')
def publicar():
	return render_template('publicar.html')

#ruta para obtener los datos de la publicacion
@app.route('/publicado', methods=['POST'])
def crearPublicacion():
	titulo = request.form['titulo']
	descripcion = request.form['descripcion']
	facilidades = request.form.getlist('facilidad')#lista con las facilidades
	habitaciones = request.form['habitaciones']
	banos = request.form['banos']
	estacionamientos = request.form['estacionamientos']
	precio = request.form['precio']
	ubicacion = request.form['posicion']
	correo = request.form['correo']
	telefono = request.form['telefono']
	nuevaPublicacion = backend.publicacion(titulo,descripcion, facilidades, habitaciones, banos, estacionamientos, precio, ubicacion, correo, telefono)
	nuevaPublicacion.guardar()
	return render_template('publicacion.html', titulo=titulo, descripcion=descripcion, 
						  habitaciones=habitaciones, banos=banos, estacionamientos=estacionamientos,
						  precio=precio, correo=correo, telefono=telefono, facilidades=facilidades, ubicacion=ubicacion)
	
#ruta para la aplicacion
#recibe: objeto publicacion
@app.route('/publicacion/<titulo>')
def publicacion(titulo):
	pub = backend.buscarPublicacion(titulo)#instancia de objeto publicacion
	return render_template('publicacion.html', titulo=pub.titulo, descripcion=pub.descripcion, habitaciones= pub.habitaciones, 
							banos=pub.banos, estacionamientos=pub.estacionamientos,
							precio=pub.precio, correo=pub.correo, telefono=pub.telefono, facilidades=pub.facilidades )

#ejecuta la app
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8000)

