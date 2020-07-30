"""
Nombre:Punto.py
Objetivo: Muestra como trabajar en objetos con python
Autor:Abel Romero Ruiz
Fecha:30 de julio 2020
"""

class Punto():
	# Definir una especie de constructor
	def __init__(self,valorX,valorY):
		#definimos el nombre de los atributos del objeto o variables
		self.x = valorX
		self.y = valorY
	#LIsta de metodos get
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	#Lista de metodos set
	def setX(self,valorX):
		#Asignar el argumento al atributo del objeto
		self.x = valorX
	def setY(self,valorY):
		self.y = valorY
	#método roString valores de los atributo x y y 
	def toString(self):
		return "Las cordenadas del punto son: X:{} , Y:{}".format(self.getX(),self.getY())
#Fin de clase



