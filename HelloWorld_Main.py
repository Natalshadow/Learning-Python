#tentative d'autentifier un User
import sys
import random
attempts = 0
list = [1, 2, 3]
print(list)

#fake authentication function
def authenticate():

    for attempts in range(5):
        print("Enter ID: ")
        ID = input()
        ID = ID.upper()

        if ID == 'EXIT':
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

#GuessGame is working as intended
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

#my own collatz attempts, it's messy and unoptimized, not even working as intended.
def collatzOWN():
    number = random.randint(2,99)
    n = number % 2

    print(number)
    print(n)
    #even number
    if n == 0:
        while number != 0:
            number = number // 2
            print(number)

    elif n == 1:
        while number != 0:
            number = 3 * number + 1
            print(number)

    else:
        print('Unforseen error, exiting.')
        sys.exit()

#the collatz used as reference, to check behaviours and results.
def collatz():
    number = random.randint(2, 99)

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

#List exercise - not yet understood how to use the list in the input and not rely on strings.
def magicBall():
    messages = ['Australia',
                'Brazil',
                'Venezuela',
                'USA']
    print(messages)

    print(messages[random.randint(0, len(messages) -1)])



#function selector
print('What do you want to do ?')
liste = ['Number Guess',
         'Collatz by Me',
         'Collatz by Git',
         'MagicBall of Trips']
print('Your options are : %s ' % (liste))
selection = input()

#I want to get rid of these and make it as short as possible relying on lists
if selection == "1":
    guessGame()

elif selection == "2":
    collatzOWN()

elif selection == "3":
    collatz()

else:
    sys.exit()

