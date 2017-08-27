#This is an attempt to have a distinct file for a series of functions and unclutter the main.py
import sys, random
def guessGame():
    secretNumber = random.randint(1, 20)

    print('#Initializing hp var...\n')
    for hp in range(6, 0, -1):
        hp -= 1
        print(hp)
    print('Ready...\n')

    print('Guess the number, come on ! You have five attempts!\n')

    for hp in range(5, 0, -1):
        guess = int(input())
        hp_init = 5
        guessesTaken = hp_init - hp

        if guess > secretNumber:
            hp = hp - 1
            print('Too high, try again.')
            print('You have ' + str(hp) + ' attempts left')
            print(hp)
            guessesTaken = hp_init - hp
            print(str(guessesTaken))
            continue
        elif guess < secretNumber:
            hp = hp - 1
            print('Too low, try again')
            print('You have ' + str(hp) + ' attempts left')
            print('HP : ' + str(hp))
            guessesTaken = hp_init - hp
            print('guessesTaken = ' + str(guessesTaken))
            continue
        else:
            break

    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

def magicBall():

    message = ['Brazil',
               'Australia',
               'USA']
    print('You shall go to : ')
    print(message[random.randint(0, len(message) - 1)])