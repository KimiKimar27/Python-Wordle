"""
DATA FILE STRUCTURE
line 1: first row wins
line 2: second row wins
line 3: third row wins
line 4: fourth row wins
line 5: fifth row wins
line 6: total wins
line 7: total losses
"""

from termcolor import colored

def reset_data():
  print(colored("Data file error", "red"))
  print("Data file will be reset")
  print("This may have been caused by tampering with the data file or the data file hasn't been created yet")
  with open("data", "r+") as data_file:
    data_file.truncate(0)
    data_file.write("0\n0\n0\n0\n0\n0\n0")

def check_corruption():
  wins_calculated = 0
  # Check if file exists
  try: open("data", "r")
  except FileNotFoundError: return True

  with open("data", "r") as data_file:
    # File contents must be strictly numbers
    try: lines = [int(i) for i in data_file.readlines()]
    except ValueError: return True
    # File must contain exactly 7 lines
    if len(lines) != 7: return True
    # Sum of wins by row must be equal to total wins
    for i in range(5): wins_calculated += lines[i]
    if wins_calculated != lines[5]: reset_data()

  return False

def update_data(game_won, attempt_no):
  with open("data", "r+") as data_file:
    lines = [int(i) for i in data_file.readlines()]
    data_file.seek(0)
    if game_won:
      lines[attempt_no - 1] += 1
      lines[5] += 1
    else:
      lines[6] += 1
    for i in range(7):
      if i != 6: data_file.write(f"{lines[i]}\n")
      else: data_file.write(f"{lines[i]}")

def print_data():
  with open("data", "r") as data_file: lines = [int(i) for i in data_file.readlines()]
  wins = lines[5]
  losses = lines[6]
  for i in range(5):
    print(f"Wins by row {i + 1}: {lines[i]}")
  print("\nWins/Losses: {}/{}, Win%: {:.1%}".format(wins, losses, wins / (wins + losses)))

def access_data(game_won, attempt_no):
  if check_corruption():
    reset_data()
    print()
  update_data(game_won, attempt_no)
  print_data()