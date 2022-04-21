import random
from ascii import *
import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
list_of_sorted_words = list()
letters_guessed = ''
lives = 6
level = False

username = input('''Please enter you name!

                 Name : ''')

username_lower = username.lower()

print('Enjoy the game', username)

while level == False:
  level = input('''
                Choose a difficulty level. 
                
                Please enter one: EASY - MEDIUM - HARD
                
                Enter:  ''')
  level = level.lower()

  if level == 'easy':
    lives = 6
    level = 'easy'
  elif level == 'medium':
    lives = 5
    level = 'medium'
  elif level == 'hard':
    lives = 4
    level = 'hard'
  elif level != 'easy' or level != 'medium' or level != 'hard':
    level = False
    print(' ')
    print('----------------------------')
    print(' ')
    print('Incorrect input, Try again.')
    print(' ')
    print('----------------------------')
    print(' ')
    

with open('words.txt') as file_object:
  file_data = file_object.readlines()
for words in file_data:
  words2 = words.strip()
  list_of_sorted_words.append(words2)
hangman_word = random.choice(list_of_sorted_words).upper()
print(' ')
print('Welcome to Hangman! The word to guess has ' + str(len(hangman_word)) + ' letters.')
 


if lives == 6:
  print(lives6)
  print(' ')
elif lives == 5:
  print(lives5)
  print(' ')
elif lives == 4:
  print(lives4)
  print(' ')
elif lives == 3:
  print(lives3)
  print(' ')
elif lives == 2:
  print(lives2)
  print(' ')
elif lives == 1:
  print(lives1)
  print(' ')

while lives > 0:
  guess = input('''
                
  Please guess a letter? ''').upper()
  if guess in hangman_word and len(guess) == 1 and guess in alphabet:
    letters_guessed = letters_guessed + guess
    print(' ')
    print('Bingo!, the letter ' + guess + ' was correct!')
    print(' ')
    print(' ')
    print('LETTERS GUESSED SO FAR:' + letters_guessed)
    print(' ')
  elif len(guess) > 1 or guess not in alphabet:
    print(' ')
    print('Invalid input')
    print(' ')
  else:
    lives -= 1
    letters_guessed = letters_guessed + guess
    print(' ')
    print(' ')
    print('LETTERS GUESSED SO FAR:' + letters_guessed)
    print(' ')
    print('Oops, that was wrong!')
    print(' ')
  bad_letter = 0

  if lives == 5:
    print(lives5)
    print(' ')
  elif lives == 4:
    print(lives4)
    print(' ')
  elif lives == 3:
    print(lives3)
    print(' ')
  elif lives == 2:
    print(lives2)
    print(' ')
  elif lives == 1:
    print(lives1)
    print(' ')

  for letter in hangman_word:
    if letter in letters_guessed:
      print(letter, end='') # end='', in short replaces the default \n so that next letter prints on same line 
    else:
      print('-', end='')
      bad_letter += 1

  if bad_letter == 0:
    print(' ')
    print('Congrats ' + username.title() + '!, The word was ' + hangman_word + '. You are a winner!')
    break

else:
  print('Oops, you ran out of lives.')
  print(' ')
  print('The word was ' + hangman_word)
  print(lives0)
      
  
