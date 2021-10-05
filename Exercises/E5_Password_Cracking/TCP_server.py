import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 1024

def Start_server():
    print("Starting server")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)

    conn, address = sock.accept()
    print('Connection address: ', address)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data : break 
        conn.send(data)
    conn.close

Start_server()
