import json
import argparse
import random
import string

parser = argparse.ArgumentParser(description="generate a random password")
parser.add_argument("-l","--length", type=int, metavar="", help="number of characters in the password")
parser.add_argument("-c","--capital", default=True, action="store_false", help="exclude capital letters")
parser.add_argument("-n","--numbers", default=True, action="store_false", help="exclude numbers")
parser.add_argument("-s","--special_characters", default=True, action="store_false", help="exclude special characters")
args = parser.parse_args()

with open('config.json') as json_file:
    data = json.load(json_file)

if args.length == None:
    length = data["length"]
else:
    length = args.length
    
if args.capital == None:
    capital = data["capital"]
else:
    capital = args.capital
    
if args.numbers == None:
    numbers = data["numbers"]
else:
    numbers = args.numbers
    
if args.special_characters == None:
    special_characters = data["special_characters"]
else:
    special_characters = args.special_characters

characters = list(string.ascii_lowercase)

if capital == True:
    characters.extend(list(string.ascii_uppercase))

if numbers == True:
    characters.extend(list(string.digits))

if special_characters == True:
    characters.extend(list(string.punctuation))

password = ""

for i in range(0, length+1):
    password += random.choice(characters)

print(password)
