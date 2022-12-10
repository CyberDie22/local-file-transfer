import socket, sys

file = sys.argv[1]

HOST = '10.0.0.186'
PORT = 50000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open(file, "rb") as f:
        data = f.read()
        s.sendall(data)
