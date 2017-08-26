#tentative d'autentifier un User
import sys
import random
attempts = 0

def authenticate():

    for attempts in range(5):
        print("Enter ID: ")
        ID = input()

        if ID == 'exit':
            print('Exiting...\n')
            sys.exit()

        elif ID == 'JOE':
            print('Enter password: ')
            password = input()
            if password == 'swordfish':
                break


        else:
            print('Wrong ID. ')
            attempts += 1
            print(attempts)
            if attempts == 5:
                print('No more tokens, wait two hours. Password changed, contact admin')
                # figure how to setup a timer
                password = 'fishtank'
                sys.exit()

            continue

    print('Access granted')
    return

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

authenticate()

print('What do you want to do ?')
print('1- Play Number Guess')
selection = input()

if selection == "1":
    guessGame()

else:
    sys.exit()

