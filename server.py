import socket

HOST = ''
PORT = '50000'

file = b''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            file += data
        with open("output.bin", "wb") as f:
            f.write(file)
            file = b''
