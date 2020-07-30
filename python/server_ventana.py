
"""
Nombre:server_ventana.py
Objetivo: recibir los datos de una ventana y enviarlos por sockets
Autor:Abel Romero Ruiz
Fecha:29 de julio  de 2020
"""
#!/usr/bin/env python3

import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)



print("Esperando... server encendido!!!")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

