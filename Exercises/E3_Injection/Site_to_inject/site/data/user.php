<?php
    print "<!DOCTYPE html><html lang=\"en\" style=\"background-color: white;\"><head><link href=\"../main.css\" rel=\"stylesheet\"></head><body><div><p>Setup A New User</p>";
    $emailAt = 0;
    $emailPeriod = 0;

    // Get the parameters from the site
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Check to see if any of them are empty
    if (($username == "") || ($email == "") || ($password == "")) {
    printError("All feilds must be used");
    }

    // Check email needs one '@' and one '.' after '@'
    $emailLen = strlen($email);
    $usernameLen = strlen($username);
    for ($i = 0; $i < $emailLen; $i++) {
        if ((!ctype_alnum($email[$i])) and ($email[$i] != '@') and 
        ($email[$i] != '.') and ($email[$i] != '-')) {
            printError("Invalid character found in email.");
        } elseif ($email[$i] == '@') {
            $emailAt = $emailAt + 1;
        } elseif (($email[$i] == '.') and ($emailAt > 0)) {
            $emailPeriod = $emailPeriod + 1;
        }
    }

    if (($emailAt != 1) or ($emailPeriod != 1)) {
        printError("Invaild email address.");
    }

    // Usernames can be made up of aphanumeric chars and '.'
    for ($i = 0; $i < $usernameLen; $i++) {
        if (!ctype_alnum($username[$i]) and $username[$i]!='.') {
            printError("Invalid character found in username.");
        }
    }

    $account = fopen("./users/" . $username, 'w+') or printError("Error in creating user");

    $data = $password . "\n" . $email;

    fwrite($account, $data);
    fclose($account);

    print "<p>$username has been added as a new user!</p>";
    endPage("true");

    function printError( $error ) {
        print "<p>Sorry, we could not create an account:</p>\n";
        print "<p>${error}</p>\n";
        endPage("false");
        die();
    }

    function endPage($created) {
        if ($created == "true") {
            print "<a href=\"../../index.html\"><button>Go Back</button></a></div></body></html>";
        } else {
            print "<a href=\"../signup.html\"><button>Go Back</button></a></div></body></html>";
        }
        
    }

?>
