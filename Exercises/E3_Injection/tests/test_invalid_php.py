import requests
EXPECTED = "test@test.com"

SESSION = requests.Session()
PATH_CREATE = 'http://localhost/site/data/user.php'
PHP = '<?php $file = file_get_contents(\'../admin\', true); print $file ?>'
USER = {'username': 'exploitNoWork.php', 'email': 'test@test.com', 'password': PHP}
ACCOUNT = SESSION.post(PATH_CREATE, data=USER)

PATH_EXPLOIT = 'http://localhost/site/data/users/exploitNoWork.php'
ADMIN = SESSION.post(PATH_EXPLOIT)

if EXPECTED == ADMIN.text:
    print("Invalid PHP Success!")
else:
    print("Invalid PHP Fail")