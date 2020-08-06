"""
Nombre:CrudListas.py
Objetivo:Archivo muestra un CRUD de listas en python
Autor:Abel Romero Ruiz
Fecha:5 de agosto  de 2020
"""

from os import system, name #Agregamos la libreria de system para poder limpiar la pantalla
#Declaramos una lista como variable global 
lista = []

#Función para agragar elementos a la lista
def addElement():
	print("\n")
	print("---- Menu agregar ----")
	print("\n")
	element = input("Nombre: ")
	lista.append(element)
	print("Elemento agregado con exito !!!")

#Función para eliminar elementos a la lista
def delElement():
	print("\n")
	print("---- Menu eliminar ----")
	print("\n")
	showElement()
	print("Escribe numero del elemento a eliminar")
	element = int(input(">"))
	lista.pop(element)
	print("Elemento eliminado con exito !!!")

#Función para cambiar elementos a la lista
def editElement():
	print("\n")
	print("---- Menu editar ----")
	print("\n")
	showElement()	
	element = input("Nombre:")
	idelement = lista.index(element)
	valorelement = input("Escribe nuevo valor:")
	lista[idelement] = valorelement
	print("Elemento editado con exito")
#Función para buscar elementos a la lista
def searchElement():
	print("\n")
	print("---- Menu buscar ----")
	print("\n")
	try:
		element = input("Escribe el elemento que deceas busacar:")
		idelement = lista.index(element)
		print("Elemento localizado:",lista[idelement])
	except ValueError as error:
		print("Este valor no existe:",element)
def showElement():
	i = 0
	for elementlist in lista:
		print(i,"-", elementlist)
		i+=1
def menu():
	print("\n")
	print("---- Menu Principal ----")
	print("\n")
	print("1.- Agregar elementos")
	print("2.- Eliminar elementos")
	print("3.- Cambiar elementos")
	print("4.- Buscar elementos")
	print("5.- Imprimir elementos")
	print("6.- Salir")
def main():
	salir = False
	while not salir:		
		menu()
		print("\n")
		try:
			print("Escribe una opción")
			ciclo = int(input(">"))
			if ciclo == 1:
				#invocar función para agregar elemnto
				system('clear')
				addElement()	
			elif ciclo == 2:
				system('clear')
				delElement()
			elif ciclo == 3:
				system('clear')
				editElement()
			elif ciclo == 4:
				system('clear')
				searchElement()
			elif ciclo == 5:
				system('clear')
				showElement()
			elif ciclo == 6:
				salir = True
				print("-----Final del programa-----")
			else:
				system("clear")
				print("Esta no es una opción!!!!")
		except ValueError as error:
			system("clear")
			print("Selecciona numeros no letras !!")
if __name__ == "__main__":
	main()
