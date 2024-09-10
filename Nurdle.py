#Numble
import random
guess = ""
hint = ""
secret_number = ""
random_number = ""
tries = 0

#Get difficulty
while True:
  print("Easy = 3 digits \nMedium = 5 digits \nHard = 7 digits \n")
  difficulty = input("Enter difficulty level: ").lower()
  if difficulty == "easy":
    difficulty = 3
    break
  elif difficulty == "medium":
    difficulty = 5
    break
  elif difficulty == "hard":
    difficulty = 7
    break
  else:
    print("Enter a valid difficulty \n")

#Generate random number based on difficulty and make sure no digits repeat
while len(secret_number) < difficulty:
  random_number = str(random.randint(0, 9))
  if random_number not in secret_number:
    secret_number += random_number

#Gets and validates guess
while True:
  guess = input("Enter guess: ")
  if len(guess) == difficulty and guess.isdigit():
    break
  else: 
    print("Invalid guess \n")
tries = tries + 1

#While guess is not secret number
while guess != secret_number:

  #Produce hint
  hint = ""
  for x in range(len(guess)):
    if guess[x] == secret_number[x]:
      hint += "G" 
    elif guess[x] in secret_number:
      hint += "Y"
    else:
      hint += "B"
  print("Hint:", hint, "\n")
  
  #Gets and validates guess
  while True:
    guess = input("Enter guess: ")
    if len(guess) == difficulty and guess.isdigit():
      break
    else: 
      print("Invalid guess \n")
  tries = tries + 1

if (difficulty+1)/2 >= tries:
  print("Amazing Performance!")
else:
  print("Good Job!")