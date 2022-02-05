### TO-DO ###
# Show available letters

### MODULES ###
import colorama
import os
from termcolor import colored
from random import randrange

### VARIABLES AND INITIALIZATION ###
with open("dictionary_user.txt", "r") as dict_file:
  WORD_LIST_USER = [line.strip() for line in dict_file]
with open("dictionary.txt", "r") as dict_file:
  WORD_LIST = [line.strip() for line in dict_file]
game_won = False
word_id = randrange(len(WORD_LIST))
board = ["_____"] * 5
os.system("title PyWordle")
colorama.init()

### FUNCTIONS ###
def word_check(word):
  global game_won
  colors = ["yellow"] * 5
  checked_word = ""

  if word == WORD_LIST[word_id]:
    game_won = True
    checked_word = colored(word, "green")
    return checked_word

  for i in range(5):
    if word[i] not in WORD_LIST[word_id]:
      colors[i] = "white"
    if word[i] in WORD_LIST[word_id]:
      colors[i] = "red"
    if word[i] == WORD_LIST[word_id][i]:
      colors[i] = "green"   
    checked_word += colored(word[i], colors[i])
  
  return checked_word

def word_attempt():
  attempt = input("Enter a five letter word: ")

  if len(attempt) != 5:
    print_board()
    print("This is not a five letter word. Please try again.")
    return word_attempt()
  if attempt not in WORD_LIST_USER:
    print_board()
    print("Word not in dictionary.")
    return word_attempt()

  return attempt

def print_board():
  os.system("cls")
  for j in range(5):
      print(board[j])

### PROGRAM ###
print_board()
i = 0
while i < 5 and game_won == False:
  attempt = word_attempt()
  print(attempt)
  board[i] = word_check(attempt)
  print_board()
  i += 1

if game_won == True:
  print("\nYou found the correct word!")
else:
  print(f"\nOut of attempts\nThe word was {WORD_LIST[word_id]}\nGame over")