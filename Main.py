import random
import sys
import datetime
import time

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

#my own collatz attempts, it's messy and unoptimized, not even working as intended.
def collatzOWN():


#the collatz used as reference, to check behaviours and results.
def collatz():
    number = int(input())
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            return number // 2

        elif number % 2 == 1:
            result = 3 * number + 1
            print(result)
            return result

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
    from Games import guessGame
    guessGame()

elif selection == "2":
    collatzOWN()

elif selection == "3":
    collatz()

elif selection == "4":
    from Games import magicBall
    magicBall()
else:
    sys.exit()

