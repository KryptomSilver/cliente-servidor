
"""
Nombre:Cilindro.py
Objetivo: es para calcular el volumen de un cilindro
Autor:Abel Romero Ruiz
Fecha:30 de julio  de 2020
"""
from Circunferencia import Circunferencia
import math 
class Cilindro(Circunferencia):
    #DEFINIMOS EL CONSTRUCTOR
    def __init__(self,valorX,valorY,valorRadio,valorAltura):
       
        #CONSTRUCTOR DE CIRCUNFERENCIA
        Circunferencia.__init__(self,valorRadio,valorX,valorY)
        #constructor de cilindro
        self.altura=valorAltura

    def getAltura(self):
        return self.altura
    def setAltura(self,valorAltura):
        self.altura = valorAltura
    def toString(self):
        return Circunferencia.toString(self)+" y la altura es: "+str(self.altura) +" el volumen es: "+self.getVolumen()
    def getVolumen(self):
        return str(Circunferencia.getArea(self)*self.getAltura())
c = Cilindro(2,3,4,5)
print(c.toString())
#hacer ventana de captura de atrubutos de objetos con tkinter