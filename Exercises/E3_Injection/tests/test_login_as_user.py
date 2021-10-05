import requests
EXPECTED = "<!DOCTYPE html><html lang=\"en\" style=\"background-color: white;\"><head><link href=\"../main.css\" rel=\"stylesheet\"></head><body><div><p>Login</p><a href=\"../../index.html\"><button>Continue to site</button></a></div></body></html>"

SESSION = requests.Session()
PATH_CREATE = 'http://localhost/site/data/user.php'
USER = {'username': 'test', 'email': 'test@test.com', 'password': 'password'}
ACCOUNT = SESSION.post(PATH_CREATE, data=USER)

PATH_LOGIN = 'http://localhost/site/data/login.php'
LOGIN_INFO = {'username': 'test', 'password': 'password'}
LOGIN = SESSION.post(PATH_LOGIN, data=LOGIN_INFO)

if EXPECTED == LOGIN.text:
    print("Login user success!")
else:
    print("Login user fail")