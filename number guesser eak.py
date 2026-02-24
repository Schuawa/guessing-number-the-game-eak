import random
secret = random.randint(1, 100)
guess = 0
attempts = 0
win = 0
print("Welcome to Guessing Game")
print("Guess number between 1 and 100")
while guess != secret:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        print("Attempts:", attempts)
if attempts > 5:
  print("you lose make sure to guess under 5 guesses")
  print("win=", win)
elif attempts > 2:
  print("great job but not perfect yet ;)")
  win += 1
  print("win=", win)
else :
  print("perfect score!!")
  win += 1
  print("win=", win)
