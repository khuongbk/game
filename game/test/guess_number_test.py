import random
print("what is your name?")
name = input()
print('welcome ' + name + ' I am thinking about a number. Can you guess it ?')
random_number = random.randint(1,20)
guess_token=0
while guess_token < 6 :
    print ('number You guess: ')
    number = int(input())
    guess_token +=1
    if number > random_number:
        print ('too high')
    if number < random_number:
        print ('too low')
    if number == random_number:
        break
if number == random_number :
    print ('that is amazing ')
if number !=random_number :
    print ('Stupid')
