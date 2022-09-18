import random

def randomChoice():
    return random.choice(['rock', 'paper', 'scissors'])

print("Welcome to Rock, Paper, Scissors!")
print("Make your choice: rock, paper, or scissors")

computerChoice = randomChoice()
userChoice = input('What is your choice? \n')

if computerChoice == userChoice:
    print(f'Computer chose {computerChoice}. You chose {userChoice}.')
    print('Draw!')
elif userChoice == 'rock' and computerChoice == 'scissors':
    print(f'Computer chose {computerChoice}. You chose {userChoice}.')
    print('You win!')
elif userChoice == 'paper' and computerChoice == 'rock':
    print(f'Computer chose {computerChoice}. You chose {userChoice}.')
    print('You win!')
elif userChoice == 'scissors' and computerChoice == 'paper':
    print(f'Computer chose {computerChoice}. You chose {userChoice}.')
    print('You win!')
else:
    print(f'Computer chose {computerChoice}. You chose {userChoice}.')
    print('You lose :( Computer wins :D') 
