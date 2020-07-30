
"""
Nombre:MainPunto.py
Objetivo: muestra multiples archivos en python
Autor:Abel Romero Ruiz
Fecha:30 de julio  de 2020
"""
#Incluir archivo de la clase
from Punto import Punto


#Creamos objetos dentro del mismo archivo
puntoA = Punto(2,3)
#invocamos los metodos get
print("El valor de la cordenada X es:",puntoA.getX())
print("El valor de la cordenada Y es:",puntoA.getY())
#invocamos metodos set
puntoA.setX(23)
puntoA.setY(12)
#Imprimimos los valores de los atributos del objeto puntoA
print(puntoA.toString())


puntoB = Punto(4,6)
#invocamos los metodos get
print("El valor de la cordenada X es:",puntoB.getX())
print("El valor de la cordenada Y es:",puntoB.getY())
#invocamos metodos set
puntoB.setX(-12)
puntoB.setY(23)
#Imprimimos los valores de los atributos del objeto puntoA
print(puntoB.toString())