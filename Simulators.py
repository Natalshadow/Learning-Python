#File containing functions that are designed to simulate stuff


def incomesProjection():

        print("This function estimates, without disturbing factors, how much incomes you will earn over the course of a given amount of time.")
        print("Income : ")
        income = int(input())
        print('In how much time :')
        duration = int(input())

        result = duration * income

        print(result)

incomesProjection()