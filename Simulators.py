#File containing functions that are designed to simulate stuff
import sys

def incomesProjection():

        print("This function estimates, without disturbing factors, how much incomes you will earn over the course of a given amount of time.")
        print("Income : ")
        income = int(input())
        print('In how much time :')
        duration = int(input())

        result = duration * income

        print(result)

def tauxRemplissage():
    listLocataires = []
    while True:
        print("Entrer nouveau locataire, print pour afficher la liste, exit pour terminer le programme.")
        locataire = input()
        if locataire == "exit":
            sys.exit()
        elif locataire == "print":
            print(listLocataires)
        else:
            listLocataires.append(locataire)



def simuTauxImposition():

    RSI = 33
    revenu = 2
    recouvrement = 0
    fraisConsulaire = 0

    resultat = RSI + revenu + recouvrement + fraisConsulaire
    taux = resultat/100

    print('This function is used to calculate the tax rate : ')

    print('Auto Entreprise : %s' %(resultat))
    print('Entrez un CA pour simuler vos charges : ')
    CA = int(input())
    result = (taux * CA)

    print(result)

simuTauxImposition()