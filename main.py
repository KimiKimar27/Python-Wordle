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
key_colors = {
  "q": "white",
  "w": "white",
  "e": "white",
  "r": "white",
  "t": "white",
  "y": "white",
  "u": "white",
  "i": "white",
  "o": "white",
  "p": "white",
  "a": "white",
  "s": "white",
  "d": "white",
  "f": "white",
  "g": "white",
  "h": "white",
  "j": "white",
  "k": "white",
  "l": "white",
  "z": "white",
  "x": "white",
  "c": "white",
  "v": "white",
  "b": "white",
  "n": "white",
  "m": "white"
}
KEY_LIST = list(key_colors)
ERASE = '\x1b[1A\x1b[2K'
os.system("title PyWordle")
os.system("title PyWordle - {}".format(WORD_LIST[word_id]))
colorama.init()

### FUNCTIONS ###
def word_check(word):
  global game_won
  colors = ["white"] * 5
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
  attempt = input("Enter a five letter word: ").lower()

  if len(attempt) != 5:
    print(f"{ERASE}{ERASE}This is not a five letter word.")
    return word_attempt()
  if attempt not in WORD_LIST_USER:
    print(f"{ERASE}{ERASE}Word not in dictionary.")
    return word_attempt()

  return attempt

def print_board():
  for i in range(5):
      print(board[i])

def print_keyboard():
  for i in range(10):
    print(colored(KEY_LIST[i], key_colors[KEY_LIST[i]]), end = " ")
  print("\n ", end = "")
  for i in range(10, 19):
    print(colored(KEY_LIST[i], key_colors[KEY_LIST[i]]), end = " ")
  print("\n   ", end = "")
  for i in range(19, 26):
    print(colored(KEY_LIST[i], key_colors[KEY_LIST[i]]), end = " ")
  print()

def print_screen():
  os.system("cls")
  print_board()
  print()
  print_keyboard()
  print()

### PROGRAM ###
print_screen()
i = 0
while i < 5 and game_won == False:
  board[i] = word_check(word_attempt())
  print_screen()
  i += 1

if game_won == True:
  print("\nYou found the correct word!")
else:
  print("\nOut of attempts")
  print(f"The word was {WORD_LIST[word_id]}")
  print("Game over")