import time
import random
def choicecave():
    cave = ''
    while cave != '1' and callable !='2':
        print('please choice')
        cave=input()
    return cave     
def display():
    print('you are front of 2 caves. ')
    print('chose cave, please!')
    print('1 or 2 ? DM')
    
def main(cave):
    print('you are fron of ....')
    time.sleep(2)
    print('fuck')
    time.sleep(2)
    print()
    random1=random.randint(1,2)
    if cave== str(random1):
        print("kakak")
    else:
         print("vcl")

play="yes"
while play == 'yes' or play == 'y':
    display()
    cave=choicecave()
    main(cave)
    print('do you want play again? yes or no')
    play=input()