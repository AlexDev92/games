import random
from time import sleep


userRollDice = input('Type "roll" to roll the dice: ')

roll = random.randint(1, 6)

computerFirstDice = random.randint(1, 6)
computerSecondDice = random.randint(1, 6)
computerTotal = computerFirstDice + computerSecondDice

if userRollDice == "roll":
    userFirstDice = random.randint(1, 6)
    userSecondDice = random.randint(1, 6)
    userTotal = userFirstDice + userSecondDice
    print(f'Your dices rolls...')
    sleep(3)
    print(f'Your first dice is: {userFirstDice} and second is: {userSecondDice} ')
    sleep(1)
    print(f'Your grand total is: {userTotal}')
    sleep(1)
    print(f'Computer dices rolls...')
    sleep(3)
    print(f'Computer first dice is: {userFirstDice} and second is: {userSecondDice} ')
    sleep(1)
    print(f'Computer grand total is: {userTotal}')
    sleep(1)
    if userTotal < computerTotal:
        print(f'Computer grand total is {computerTotal} and yours is {userTotal}')
        sleep(1)
        print(f'Computer WINS!')
    elif userTotal > computerTotal:
        print(f'Your grand total is {userTotal} and computer is {computerTotal}')
        sleep(1)
        print(f'You WINS!')        
else:
    print('Bad input!')
