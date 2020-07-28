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
	if (n2!=0):
		return n1 / n2
	else:
		print("Error en la division no se puede dividir entre 0")
def compara(n1,n2):
	if n1>n2:
		print("El mayor es n1: ",n1," ",n2)
	elif n2>n1:
		print("El mayor es: {},{}".format(n2,n1))
	else:
		print("Los numeros son iguales: {},{}".format(n1,n2))
#funcion para mostrar operación de for
def cuenta(n1,n2):
	if(n2>n1):
		for i in range(n1,n2+1):
			print("Valor de i:{}".format(i))
	elif(n1>n2):
		for i in range(n1, n2-1,-1):
			print("Valor de i:{}".format(i))
	else:
		print("Los numeros son iguales:{},{}".format(n1,n2))
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
		compara(a,b)
		cuenta(a,b)
		ciclo = input("Desea otra operacion (s/n)?: ")
	else:
		print("Fin de programa")
if __name__ == "__main__":
	main()
