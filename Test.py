# Adding user input to a list
import sys

def list_try():
    liste = []

    while True:
        print('List trial, input items: ')
        item = input()
        item.lower()


        if item == "exit":
            print('Entered exit, exiting.')
            sys.exit()

        elif item == "print":
            print(liste)

        else:
            liste.append(item)


list_try()