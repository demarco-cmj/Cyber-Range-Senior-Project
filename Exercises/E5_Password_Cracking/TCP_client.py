import socket
import time
import random
import string
import os.path
from os import path
import importlib

moduleName = 'PasswordMaker'
importlib.import_module(moduleName)

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

def Start_client():
    print("starting client")
    TCP_IP = '127.0.0.1'
    TCP_PORT = 12345
    BUFFER_SIZE = 1024
    PWlist = retrive_passwords()
    Message = FindMessage(PWlist)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((TCP_IP, TCP_PORT))
    while True:
        for string in Message:
            string.replace('\n','')
            sock.send(string.encode())
            value = random.randint(0,5)
            time.sleep(value)


    data = sock.recv(BUFFER_SIZE)
    sock.close()

    print ("recieved data: ", data)

Start_client()