"""
DATA FILE STRUCTURE
line 1: first row wins
line 2: second row wins
line 3: third row wins
line 4: fourth row wins
line 5: fifth row wins
line 6: total wins
line 7: total losses
line 8: streak type - loss (0) or win (1)
line 9: streak count
"""

from termcolor import colored

def reset_data():
  print(colored("Data file error", "red"))
  print("Data file will be reset")
  print("This may have been caused by tampering with the data file or the data file hasn't been created yet")
  with open("data", "w") as data_file:
    data_file.write("0\n0\n0\n0\n0\n0\n0\n0\n0")

def check_corruption():
  wins_calculated = 0
  # Check if file exists
  try:
    open("data", "x")
    return True
  except FileExistsError:
    pass
    

  with open("data", "r") as data_file:
    # File contents must be strictly numbers
    try: lines = [int(i) for i in data_file.readlines()]
    except ValueError: return True
    # File must contain exactly 9 lines
    if len(lines) != 9: return True
    # Sum of wins by row must be equal to total wins
    for i in range(5): wins_calculated += lines[i]
    if wins_calculated != lines[5]: return True
    # Streak type must be strictly a 1 or a 0
    if lines[7] not in (0, 1): return True
    # Streak count can't be larger than win/loss totals
    if lines[7] == 0 and lines[6] < lines[8]: return True
    if lines[7] == 1 and lines[5] < lines[8]: return True

  return False

def update_data(game_won, attempt_no):
  with open("data", "r+") as data_file:
    lines = [int(i) for i in data_file.readlines()]
    data_file.seek(0)
    # If streak type has changed, set streak count to 0, if not, increment streak count by 1
    if (lines[7] == 0 and game_won == True) or (lines[7] == 1 and game_won == False): lines[8] = 1
    else: lines[8] += 1
    # Set streak type
    if game_won == True: lines[7] = 1
    else: lines[7] = 0
    # Update total wins/losses
    if game_won:
      lines[attempt_no - 1] += 1
      lines[5] += 1
    else:
      lines[6] += 1
    # Write new data to file
    for i in range(9):
      if i != 8: data_file.write(f"{lines[i]}\n")
      else: data_file.write(f"{lines[i]}")

def print_data():
  with open("data", "r") as data_file: lines = [int(i) for i in data_file.readlines()]
  wins = lines[5]
  losses = lines[6]
  for i in range(5):
    print(f"Wins by row {i + 1}: {lines[i]}")
  print("\nWins/Losses: {}/{}, Win%: {:.1%}".format(wins, losses, wins / (wins + losses)))
  if lines[7] == 1: print(f"You are currently on a {lines[8]} game winning streak")
  else: print(f"You are currently on a {lines[8]} game losing streak")

def access_data(game_won, attempt_no):
  if check_corruption():
    reset_data()
    print()
  update_data(game_won, attempt_no)
  print_data()
