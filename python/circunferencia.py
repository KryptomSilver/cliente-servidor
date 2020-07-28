"""
Nombre:Circunferencia.py
Objetivo: Permite calcular el área de una circunferencia
Autor:Abel Romero Ruiz
Fecha:28 de julio de 2020
"""

#Importamos libreria math
import math as m

#función para calcular el área
def calculararea(valorRadio):
	return m.pi*m.pow(valorRadio,2)
#Módulo principal
def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':
		print("--- Programa para calcular de circunferencia ---")
		vradio = int(input("Introduce valor del radio: "))
		print("El área de la circunferencia con radio igual a:{}, es:{}".format(vradio,calculararea(vradio)))
		ciclo = input("Otro cálculo (s/n)?")
	else:
		print("** Fin del programa")
if __name__ =="__main__":
	main()
