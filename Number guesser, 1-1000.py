Loop = True
from random import *
number = randint(1, 1000)
guess_count = 0

print("Guess a number between 1 and 1000")
while Loop == True:
  print("")
  guess = int(input())

  if guess == number:
    guess_count = guess_count + 1
    print("Congratulations! You guessed correctly in", guess_count, "attempts.")
    
  elif guess > number:
    guess_count = guess_count + 1
    print("Attempt", guess_count, "- Too high")
    
  else:
    guess_count = guess_count + 1
    print("Attempt", guess_count, "- Too low")
    
