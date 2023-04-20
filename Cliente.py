# Elaborado por Trinidad González Alan Isaac.

import socket

HOST = "localhost"
PORT = 65432
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with open("prueba.mp3", "rb") as f: # rb Lectura en modo binario.
        while True:
            size = f.read(buffer_size)
            if not size:
                break
            s.sendto(size, (HOST, PORT))
    print("Terminé")