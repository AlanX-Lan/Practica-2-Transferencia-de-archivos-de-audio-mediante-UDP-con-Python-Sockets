# Elaborado por Trinidad González Alan Isaac.

import socket
import selectors
import types

HOST = "localhost"
PORT = 65432
buffer_size = 1024
sel = selectors.DefaultSelector() # Creamos un selector de eventos.

def read_data(sock):
    data, addr = sock.recvfrom(buffer_size)
    if data:
        print(f"Recibidos {len(data)} bytes de {addr}")
        # Escribimos los datos recibidos en un archivo de audio.
        with open(f"audio{addr}.mp3", "ab") as f: # ab Agrega contenido en modo binario.
            f.write(data)
    else:
        print(f"Cerrando {addr}")
        sel.unregister(sock)
        sock.close()

# Creamos el socket del servidor y lo configuraramos para escuchar conexiones entrantes.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, read_data)
    print("El servidor UDP está disponible y en espera de solicitudes")

    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj)