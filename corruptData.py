import os
import colorama
from termcolor import cprint
from data import check_corruption, reset_data

colorama.init()

def reset_data():
  with open("data", "w") as data_file:
    data_file.write("0\n0\n0\n0\n0\n0\n0\n0\n0")

def printTestResult(err_type):
  if check_corruption():
    cprint(f"Detected corruption: {err_type}", "green")
    reset_data()
  else:
    cprint(f"Failed to detect corruption: {err_type}", "red")
    reset_data()

def notNumbers():
  with open("data", "r+") as data_file:
    data_file.write("text")
  printTestResult("notNumbers")

def fileUnderNineLinesLong():
  with open("data", "r") as data_file:
    lines = data_file.readlines()
    lines[6] = lines[6].strip()
  with open("data", "w") as data_file:
    for i in range(7):
      data_file.write(lines[i])
  printTestResult("fileUnderNineLinesLong")

def fileOverNineLinesLong():
  with open("data", "a") as data_file:
    data_file.write("\nnew line")

  printTestResult("fileOverNineLinesLong")

def winsByRowSumNotEqualToWins():
  with open("data", "r") as data_file:
    lines = data_file.readlines()
  with open("data", "w") as data_file:
    lines[0] = f"{int(lines[5]) + 1}\n"
    for line in lines:
      data_file.write(line)
  printTestResult("winsByRowSumNotEqualToWins")

def streakTypeNotValid():
  with open("data", "r") as data_file:
    lines = data_file.readlines()
  with open("data", "w") as data_file:
    for i in range(9):
      if i == 7: data_file.write("2\n")
      else: data_file.write(lines[i])
  printTestResult("streakTypeNotValid")

def winStreakCountLargerThanWinTotals():
  with open("data", "r") as data_file:
    lines = data_file.readlines()
  with open("data", "w") as data_file:
    lines[7] = "1\n"
    lines[8] = f"{int(lines[5]) + 1}\n"
    lines[-1] = lines[-1].strip()
    for line in lines:
      data_file.write(line)
  printTestResult("winStreakCountLargerThanWinTotals")

def lossStreakCountLargerThanLossTotals():
  with open("data", "r") as data_file:
    lines = data_file.readlines()
  with open("data", "w") as data_file:
    lines[7] = "0\n"
    lines[8] = f"{int(lines[6]) + 1}\n"
    lines[-1] = lines[-1].strip()
    for line in lines:
      data_file.write(line)
  printTestResult("lossStreakCountLargerThanLossTotals")

def fileDoesntExist():
  os.remove("data")
  printTestResult("fileDoesntExist")

def testAll():
  reset_data()
  # Start testing
  notNumbers()
  fileUnderNineLinesLong()
  fileOverNineLinesLong()
  winsByRowSumNotEqualToWins()
  streakTypeNotValid()
  winStreakCountLargerThanWinTotals()
  lossStreakCountLargerThanLossTotals()
  fileDoesntExist()

if __name__ == "__main__":
  testAll()