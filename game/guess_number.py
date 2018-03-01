import random

guessestaken=0
print("Hello!What is your name?")
myname=input()

print("well, " + myname + "i am thinking a number between 1 and 20.")
randomNumber=random.randint(1,20)
while guessestaken <6 :
    print("take a guess")
    guess=input()
    guess=int(guess)
    guessestaken +=1
    if guess < randomNumber :
        print("you guessed too low")
    if guess > randomNumber :
        print("you guessed to high")
    if guess == randomNumber :
        break
if guess == randomNumber :
    guessestaken = str(guessestaken)
    print("Good job, " + myname + " you guessed in " + guessestaken +" guesses ")
if guess != randomNumber :
    print("stupid!")