import random
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
def getRandomWords(words):
     wordIndex=random.randint(0,len(words))
     return words[wordIndex]    
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print("missed letter: ",end='')
    for i in missedLetters:
        print(i)
    blank='_'* len(secretWord)
    for k in range(len(secretWord)):
        if secretWord[k] in correctLetters:
            blank=blank[:k]+secretWord[k]+blank[k:]
    for letter in blank:
        print(letter,end='')
    print()
def guess(alreaydguess):
    print("you guess:")
    guess=input()
    if guess in alreaydguess:
        print("please guess again")
    elif len(guess)!=1:
        print("single letter")
    elif guess not in "qwertyuiopasdfghjklzxcvbnm":
        print("letter please")
    else:
        return guess
def playagain():
    print("do you want play again?")
    return input().lower().startswith('y')

print(" H A N G M A N")
print()
missedLetters=''
correctLetters=''
secretWord=getRandomWords(words)
gameisDone=False 
while true:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess=guess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters=correctLetters+guess
        allfoundletter=True
        for t in range(len(secretWord)):
            if secretWord not in correctLetters:
                allfoundletter=False
        if allfoundletter:
            print('that is amazing',correctLetters)
            gameisDone=True
    else:
        displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
        missedLetters=missedLetters+guess
        
   
    
            
    
 


