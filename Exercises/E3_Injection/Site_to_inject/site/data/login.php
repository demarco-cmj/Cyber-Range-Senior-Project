<?php 
    print "<!DOCTYPE html><html lang=\"en\" style=\"background-color: white;\"><head><link href=\"../main.css\" rel=\"stylesheet\"></head><body><div><p>Login</p>";
    $usernameIn = $_POST['username'];
    $passwordIn = $_POST['password'];
    
    // Check to see if any of them are empty
    if (($usernameIn == "") || ($passwordIn == "")) {
        loginError();
    }

    // Usernames can be made up of aphanumeric chars and '.'
    $usernameLen = strlen($usernameIn);
    for ($i = 0; $i < $usernameLen; $i++) {
        if (!ctype_alnum($usernameIn[$i]) and $usernameIn[$i]!='.') {
            loginError();
        }
    }

    $userIn = "./users/" . $usernameIn;
    if (!file_exists($userIn)) {
        loginError();
    }

    $user = fopen($userIn, "r");
    if (!$user) {
        loginError();
    }

    $password = fgets($user);
    $email = fgets($user);
    $passwordLen = strlen($password);
    $passwordInLen = strlen($passwordIn);

    if ($passwordInLen != $passwordLen - 1) {
        loginError();
    }
    for ($i = 0; $i < $passwordLen - 1; $i++) {
        if ($password[i] != $passwordIn[i]) {
            print($passwordIn);
            loginError();
        }
    }

    endPage("true");

    function loginError() {
        print "<p>Sorry, we could not log you in</p>\n";
        endPage("false");
        die();
    }

    function endPage($authenticated) {
        if ($authenticated == "true") {
            print "<a href=\"../../index.html\"><button>Continue to site</button></a></div></body></html>";
        } else {
            print "<a href=\"../../index.html\"><button>Go Back</button></a></div></body></html>";
        }
        
    }
?>