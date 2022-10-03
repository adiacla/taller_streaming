# echo-server.py

import socket


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9999  # Port to listen on (non-privileged ports are > 1023)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
data="Texto"
print('Esperando una conexión, inicie el cliente')
while data!=">":
    conn, addr = s.accept()
    print(f"Connected by {addr}\n")
    data=input("Texto > :")
    conn.send(bytes(data, "Utf-8"))       
    conn.close()
s.close()