import socket

Ip = "127.0.0.1"
port = 60000
buffersize = 2048

messageFromServer = "Hello client "
fromServerBytes = str.encode(messageFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind( ( Ip,port ) )

print("Serveris listening ")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMessage = "Message from Client: {}".format(message)
    clienntAdddress = "Client IP address: {}".format(address)

    print(clientMessage)
    print(clienntAdddress)

    UDPServerSocket.sendto(fromServerBytes, address)