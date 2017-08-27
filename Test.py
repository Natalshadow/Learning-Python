import random


def magicBallList():

    message = ['Brazil',
               'Australia',
               'USA']
    print('You shall go to : ')
    print(message[random.randint(0, len(message) - 1)])

magicBallList()