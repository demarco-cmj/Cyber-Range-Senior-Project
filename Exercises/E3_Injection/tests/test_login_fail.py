import requests
EXPECTED = "<!DOCTYPE html><html lang=\"en\" style=\"background-color: white;\"><head><link href=\"../main.css\" rel=\"stylesheet\"></head><body><div><p>Login</p><p>Sorry, we could not log you in</p><a href=\"../../index.html\"><button>Go Back</button></a></div></body></html>"


SESSION = requests.Session()
PATH_LOGIN = 'http://localhost/site/data/login.php'
LOGIN_INFO = {'username': 'admin', 'password': 'password'}
LOGIN = SESSION.post(PATH_LOGIN, data=LOGIN_INFO)

if EXPECTED != LOGIN.text:
    print("Fail login user success!")
else:
    print("Fail login user fail")