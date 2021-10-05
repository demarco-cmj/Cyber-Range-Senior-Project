import random
import string

def random_String():
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    numbers = string.digits
    choices = [letters_lower, letters_upper, numbers]
    password = ""
    for i in range(5):
        password = password + random.choice(choices[random.randint(0,2)])
    return password
    
def write_File(passwords):
    password_File = open("PWList.txt", "w")
    for x in passwords:
        word = x
        password_File.writelines(word)
    password_File.close
    return    

def Create_passwords():
    password_list = []
    for x in range(100): 
        if x != 0:
            password_list.append("\n" + random_String())
        else:
            password_list.append(random_String())
    write_File(password_list)

Create_passwords()