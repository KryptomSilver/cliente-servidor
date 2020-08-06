"""
Nombre:Listas.py
Objetivo:Muestra la función de las listas en python
Autor:Abel Romero Ruiz
Fecha:4 de agosto  de 2020
"""
def main():
    # Una lista es una estructura de datos en python
    lista = [1,23.01,False,"hola lista", 'A', [-1,-5,"hola",5],-12]
    #lista vacia
    listaVaciaֵ = []
    #Accesando elemntos de la lista 
    for elemento in lista:
        print("El elemnto de la lista es: ", elemento)
    for i in listaVaciaֵ:
        print("El elemnto de la lista es: ", i)
    #imprimir un elemento de la lista 
    print("Elemento en la posición 3",lista[3])
    print("Elemento en la posición 3",lista[-5])
    #print(lista[300])
    #leer un elemento que esta en la posición 2 de la lista interna 
    print(lista)
    lista.insert(5,2)
    print(lista)
    #index() imprime el indice 
    #print("La posición de la False es :",lista.index(False))
    #Eliminar elementos de la lista remove()
    lista.remove("hola lista")
    print(lista)
if __name__ == "__main__":
	main()
