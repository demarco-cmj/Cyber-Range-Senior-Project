import socket
import string
import random
import time
import os.path
from os import path


def retrive_passwords():
    if path.exists("PWList.txt") == True:
        PWD_File = open("PWList.txt", "r")
        passwords = PWD_File.readlines()
        PWD_File.close()
        return passwords
    return

def FindMessage(list):
    message = []
    for x in range(5):
        message.append(list[random.randint(0,100)])
    return message

serverAddressPort = ("127.0.0.1", 60000)

buffersize = 2048

#create UDP packet
UDPclientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
PWlist = retrive_passwords()
message = FindMessage(PWlist)

while True:
    for string in message:
        string.replace('\n', '')
        messageBytes = str.encode(string)

        UDPclientSocket.sendto(messageBytes, serverAddressPort)

        messageFromServer = UDPclientSocket.recv(buffersize)
        value = random.randint(5,10)
        time.sleep(value)

serverString = "Message from server {}".format(messageFromServer[0])
print('\n')
print(serverString)