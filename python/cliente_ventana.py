
"""
Nombre:cliente_ventana.py
Objetivo: enviar datos hacia el server con socket por medio de una ventana 
Autor:Abel Romero Ruiz
Fecha:29 de julio  de 2020
"""
#!/usr/bin/env python3
import socket
def sendToServer(text):
	arr = bytes(text, 'utf-8')
	
	HOST = 'localhost'  # The server's hostname or IP address
	PORT = 65432        # The port used by the server
	print(text)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(arr)
		data = s.recv(1024)
	print('Received', repr(data))