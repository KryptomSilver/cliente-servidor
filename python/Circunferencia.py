
"""
Nombre:Circunferencia.py
Objetivo: es para calcular la circunferencia
Autor:Abel Romero Ruiz
Fecha:30 de julio  de 2020
"""
import math
from Punto import Punto
class Circunferencia(Punto):
    #definir constructor
    def __init__(self,vradio,valorX,valorY):
        Punto.__init__(self,valorX,valorY)
        #Atributo de la circunferencia
        self.radio = vradio
    def getRadio(self):
        return radio
    def setRadio(self,vradio):
        self.radio =vradio
    def getArea(self):
        return math.pi*math.pow(self.radio,2)
    def toString(self):
        return Punto.toString(self)+"  el valor del radio es:"+str(self.radio)+"y el área:"+str(self.getArea())
