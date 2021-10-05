import requests
EXPECTED = "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n<html><head>\n<title>404 Not Found</title>\n</head><body>\n<h1>Not Found</h1>\n<p>The requested URL was not found on this server.</p>\n<hr>\n<address>Apache/2.4.41 (Ubuntu) Server at localhost Port 80</address>\n</body></html>\n"

SESSION = requests.Session()
PATH_CREATE = 'http://localhost/site/data/user.php'
PHP = '<?php $file = file_get_contents(\'admin\', true); print $file ?>'
USER = {'username': 'badEmail.php', 'email': '', 'password': PHP}
ACCOUNT = SESSION.post(PATH_CREATE, data=USER)

PATH_EXPLOIT = 'http://localhost/site/data/users/badEmail.php'
ADMIN = SESSION.post(PATH_EXPLOIT)

if EXPECTED == ADMIN.text:
    print("Empty Account Success!")
else:
    print("Empty Account Fail")