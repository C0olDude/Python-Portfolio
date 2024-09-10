import random

# write a guessing game
# generate a secret 6 digit number
secret = random.randint(100000, 999999)
print(secret)

# 78327

# write guessing game and ask the user for a 6 digit number

# initialize guess

while True:
    try:
        guess = int(input("Enter a 6 digit number: "))
        if len(str(guess)) == 6:
            break
    except:
        print("Enter a 6 digit number.")
    

while guess != secret: # while guess isn't secret
    
# after each wrong guess, give them a clue
# the clue will be the number of digits guessed correctly

    # count the digits that match (the easieat way to compare digits is when they are a string)
    matches = 0
    for i in range(6):
        if str(guess)[i] == str(secret)[i]:
            matches += 1
    print("The number of digits that match are: ", matches)
    while True:
        try:
            guess = int(input("Enter a 6 digit number: "))
            if len(str(guess)) == 6:
                break
        except:
            print("Enter a 6 digit number.")
    
  

# 18627
# then they guessed 3 digits correctly
# the game continues until the user guesses the number



