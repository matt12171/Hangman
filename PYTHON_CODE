import random
from ascii import *

list_of_sorted_words = list()
letters_guessed = ''
lives = 6




with open('words.txt') as file_object:
  file_data = file_object.readlines()
for words in file_data:
  words2 = words.strip()
  list_of_sorted_words.append(words2)
hangman_word = random.choice(list_of_sorted_words).upper()
print('Welcome to Hangman! The word to guess has ' + str(len(hangman_word)) + ' letters.')
 
print(lives6)


while lives > 0:
  print(' ')
  print(' ')
  guess = input('Please guess a letter? ').upper()
  if guess in hangman_word:
    print('Bingo!, the letter ' + guess + ' was correct!')
  else:
    lives -= 1
  letters_guessed = letters_guessed + guess
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
    print('Congrats!, The word was ' + hangman_word + '. You are a winner!')
    break

else:
  print('Oops, you ran out of lives.')
  print(lives0)
      
  
