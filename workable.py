# Write your code here
import random
import string

print("H A N G M A N")
print()
letter = ''
words = ['python', 'java', 'kotlin', 'javascript']
guess = random.choice(words)
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
tries = 8
letlist = []
hint = list("-" * len(guess))
controlvar = 0
while tries > 0:
    print()
    print("".join(hint))

    letter = (input("Input a letter: "))

    letlist.append(letter)
    if letlist.count(letter)>1:
        print("You've already guessed this letter.")
       
    if letter not in alphabet_list:
        print("Please enter a lowercase English letter")
       
    if len(letter) > 1:
        print("You should input a single letter")
        
    if letter not in guess and letter in alphabet_list and not letlist.count(letter)>1 and not len(letter)>1:
        tries -= 1
        print("That letter doesn't appear in the word")
    if letter in hint and tries >= 0:
        print("No improvements")
        

    for j in range(len(guess)):
        if letter == guess[j]:
            hint[j] = letter
    
    if "-" not in hint:
        break

print(guess)
if "-" in hint:
    print("You lost!")
else:
    print("You guessed the word!")
    print("You survived!")
