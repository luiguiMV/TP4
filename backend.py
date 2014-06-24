"""backend de la progra 4"""

import pickle#libreria utilizado para guardar los objetos en archivos.txt

#variables globales
listaPublicaciones=[]#lista que contiene objetos publicacion



"""//////////////////////////////////////////////////////////////
							CLASES
/////////////////////////////////////////////////////////////////"""
#clase publicacion
#atributos: titulo, descripcion, facilidades:lista, habitaciones, ba;os, estacionamientos, precio, correo, telefono
#metodos:
class publicacion:
	def __init__(self, titulo,descripcion, facilidades, habitaciones, banos, estacionamientos, precio, ubicacion, correo, telefono):
		self.titulo=titulo
		self.descripcion=descripcion
		self.facilidades=facilidades
		self.habitaciones=habitaciones
		self.banos=banos
		self.estacionamientos=estacionamientos
		self.precio=precio
		self.ubicacion=ubicacion
		self.correo=correo
		self.telefono=telefono
	
	def guardar(self):
		listaPublicaciones=leer()
		listaPublicaciones.append(self)
		pickle.dump(listaPublicaciones, open("datos/publicaciones.obj", "wb"))
		
		
		
"""//////////////////////////////////////////////////////////////
							FUNCIONES
/////////////////////////////////////////////////////////////////"""
#funcion leer
#Entradas: no tiene
#Salidas: retorna una lista de objetos publicacion obtenido de un archivo.obj
def leer():
	try:
		listaPublicaciones = pickle.load(open("datos/publicaciones.obj", "rb"))
		return listaPublicaciones
	except:
		return []

#funcion buscarPublicacion
#Entradas: String titulo
#Salidas:  retorna un objeto publicacion que corresponde con el titulo
def buscarPublicacion(titulo):
	lista = leer()
	for e in lista:
		if e.titulo == titulo:
			return e
			
#funcion filtrar
#Entradas: facilidades:lista Strings, habitaciones, banos, estacionamientos, precio_inicial, precio_final
#Salidas = lista de objetos publicacion que cumplen las caracteristicas
def filtrar(facilidades, habitaciones, banos, estacionamientos, precio_inicial, precio_final):
	lista = leer()
	res = []#lista que contiene los elementos para el resultado
	for pub in lista:
		if ((filtrarFacilidad(facilidades,pub.facilidades) or facilidades==[]) and (habitaciones==pub.habitaciones or habitaciones=='omitir')
		 and (banos==pub.banos or banos=='omitir') and (estacionamientos == pub.estacionamientos or estacionamientos=='omitir')
		 and ((precio_inicial<pub.precio and precio_final> pub.precio) or precio_inicial=="" or precio_final=="")):
				res.append(pub)
	
	return res
		
#funcion filtrarFacilidad
#Entradas: 2 lista de facilidades
#Salidas: True si el objeto cumple la o las facilidades, False de lo contrario
def filtrarFacilidad(facilidades, f):
	for ele in facilidades:
		if ele in f:
			pass
		else:
			return False
	return True	
	
