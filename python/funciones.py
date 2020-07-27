"""
Nombre:funciones.py
Objetivo:muestra la operacion de las funciones en python
Autor:Abel Romero Ruiz
Fecha: 27 julio de 2020
"""
def mensaje():
	print("hola desde mensaje")
def regresaMensaje():
	return "saludo desde regresaMensaje"

def printMensaje(msg):
	print(msg)
def suma(n1,n2):
	return n1 + n2
def resta(n1,n2):
	return n1 - n2
def multiplicacion(n1,n2):
	return n1 * n2 
def division(n1,n2):
	return n1 / n2
def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':
		#invocamos funcion mensaje()
		mensaje()
		#invocamos funcion 
		print(regresaMensaje())
		#invocamos 
		printMensaje("hola")
		#leer datos
		a = int(input("ingresa el primer numero entero: "))
		b = int(input("ingresa el segundo numero: "))
		print("La suma es: ",suma(a,b))
		print("La resta es: ",resta(a,b))
		print("La multplicación es: ",multiplicacion(a,b))		
		print("La división es: ",division(a,b))
		ciclo = input("Desea otra operacion (s/n)?: ")
	else:
		print("Fin de programa")
if __name__ == "__main__":
	main()
