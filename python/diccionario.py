"""
Nombre:Diccionario.py
Objetivo:Muestra la operación de los diccionarios
Autor:Abel Romero Ruiz
Fecha:5 de agosto  de 2020
"""

def main():
    #creamos diccionario
    dic = {'clave':20082133,'nombre':'Abel Romero Ruiz','edad':22 ,'cursos':["hola"]}
    #Listar items del diccionario
    print("Los items son: ",dic)
    #Imprimir un item de un diccionario proporcionando su key
    print("El valor de la key es: ", dic['cursos'][0])
    #imprimir todo el dic
    for i in dic:
        print(i,":",dic[i])
    for i in dic['cursos']:
            print(i)
    #metodos del diccionario
    #get, pop, key, clean, update
if __name__=="__main__":
    main() 