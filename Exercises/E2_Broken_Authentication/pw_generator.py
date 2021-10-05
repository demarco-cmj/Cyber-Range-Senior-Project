import random
import string
import os.path
import sys
from os  import path
import settings

""" Creates a list of potential passwords equal to num_words
    that contains a random combination of lowercase letters, 
    uppercase letters, and digits. Only run if Possible_pws 
    doesn't exist. """

def create_pw_list():
	num_words = settings.num_words
	if (num_words < 2):
		sys.exit("Error: num_words too small. Should be greater than or equal to 2.")
	if not path.exists(settings.poss_pw_file):
		file = open(settings.poss_pw_file, "w")
		"""alphabet consists of letters and numbers"""
		alphabet = string.ascii_letters + string.digits
		"""Generate passwords equal to number of words"""
		for i in range(num_words):
			strlen = random.randint(4, 8)
			word = ""
			"""Generate a single password"""
			for j in range(strlen):
				word += random.choice(alphabet)
			"""Add a new line character to the word if
			   it is not the last word. Should allow
			   for students to write scripts easier"""
			if i != num_words-1:
				word += "\n"
			file.write(word)
		file.close()
		create_pw()
        
""" Picks a random password from the generated potential
	passwords file, and stores that password in a new file."""

def create_pw():
	file = open(settings.poss_pw_file, "r")
	output = file.read()
	words = output.split()
	pw = random.choice(words)
	file2 = open(settings.pw_file, "w")
	file2.write(pw)
	file2.close()
	file.close()


create_pw_list()