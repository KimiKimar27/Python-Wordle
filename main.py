### MODULES ###
import colorama
import os
from termcolor import colored
from random import randrange
from data import access_data
from collections import Counter

### VARIABLES AND INITIALIZATION ###
with open("dictionary_user.txt", "r") as dict_file:
  WORD_LIST_USER = [line.strip() for line in dict_file]
with open("dictionary.txt", "r") as dict_file:
  WORD_LIST = [line.strip() for line in dict_file]
game_won = False
word_id = randrange(len(WORD_LIST))
ANSWER = WORD_LIST[word_id]
board = ["_____"] * 6
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
ERASE = "\x1b[1A\x1b[2K"
os.system("title PyWordle")
colorama.init()

### FUNCTIONS ###
def word_check(word):
  global game_won
  colors = ["white"] * 5
  count_guess = Counter(word)
  
  if word == ANSWER:
    game_won = True
    checked_word = colored(word, "green")
    return checked_word

  for letter in count_guess:
    answer_letter_indices = [i for i in range(5) if letter == ANSWER[i]]
    guess_letter_indices = [i for i in range(5) if letter == word[i]]
    green = set(guess_letter_indices).intersection(set(answer_letter_indices))
    red = [i for i in guess_letter_indices if i not in green][:len(answer_letter_indices) - len(green)]
  
    for i, v in enumerate(colors):
      if v == "white":
        if key_colors[word[i]] != "red" or "green": key_colors[word[i]] = "grey"
    for i in red:
      colors[i] = "red"
      if key_colors[word[i]] != "green": key_colors[word[i]] = "red"
    for i in green:
      colors[i] = "green"
      key_colors[word[i]] = "green"
  
  return ''.join([colored(word[i], colors[i]) for i in range(5)])

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
  for i in range(6):
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
while i < 6 and game_won == False:
  board[i] = word_check(word_attempt())
  print_screen()
  i += 1

if game_won == True:
  print("You found the correct word!\n")
else:
  print("Out of attempts")
  print(f"The word was {ANSWER}")
  print("Game over\n")

access_data(game_won, i)