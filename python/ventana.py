"""
Nombre:ventana.py
Objetivo: muestra como trabajar con ventanas gui en python y tkinter
Autor: Abel Romero Ruiz	
Fecha: 29 de julio de 2020
"""

#import librerias 
from tkinter import *
from tkinter import ttk
from cliente_ventana import sendToServer
#funcion para enviar datos al servidor
#Función main

def main():
	def obtener():
		variable = txtCampo.get()
		sendToServer(variable)
	#Creamos la ventana como contenedora
	win = Tk()
	#modificamos parametros de la ventana 
	win.geometry("450x200")
	win.title("Mi primer ventana en python")
	#Creamos una etiqueta
	label = ttk.Label(win,text="Texto a enviar al servidor:")
	label.grid(pady=20,padx=10,row=0,column=0)
	#txtCampo = ttk.Entry(win).pack(side=TOP)
	
	txtCampo = ttk.Entry(win,width=40)
	txtCampo.grid(pady=20,row=0,column=1,columnspan=2)
	
	#Creamos un boton en la ventana
	buttonsalir = Button(win,width=25,text="Salir",command=quit,bg="red",activebackground="red",fg="white")	
	buttonsalir.grid(pady=15,row=1,column=0,columnspan=2)
	#Creamos un botton para enviar el contenido text del entry al server
	button = Button(win,width=25,text="Enviar mensaje",command=obtener,bg="green",activebackground="green",fg="white")
	button.grid(pady=15,row=1,column=2,columnspan=2)
	#hacemos un ciclo para dibujar y esperar eventos
	win.mainloop()
	
#para funcion main
if __name__ == "__main__":
	main()
