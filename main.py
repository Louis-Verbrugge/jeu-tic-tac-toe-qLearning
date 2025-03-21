
import random

from src.Player import Player
from src.stats import historical





def endGame(table):

    return table[0] == table[1] == table[2] != '.' or \
        table[3] == table[4] == table[5] != '.' or \
        table[6] == table[7] == table[8] != '.' or \
        table[0] == table[3] == table[6] != '.' or \
        table[1] == table[4] == table[7] != '.' or \
        table[2] == table[5] == table[8] != '.' or \
        table[1] == table[4] == table[8] != '.' or \
        table[2] == table[4] == table[6] != '.' or \
        '.' not in table


def displayTable(table):

    print("\n\n")
    for i in range(len(table)-1):
        if i%3==0:
            print('')
        print(table[i], end='')


def main():
    historicalList={}
    table = ['.']*10
    player1 = Player('Joueur 1', 'X')
    player2 = Player('Joueur 2', 'O')
    playerList = (player1, player2)

    while not endGame(table):

        tableBefore = table.copy()
        table, action = playerList[0].play(table)
        historicalList = historical(historicalList, playerList[0].getName(), tableBefore, action, table)
        playerList = tuple(reversed(playerList))
        displayTable(table)

    return historicalList

historicalList = main()
print("\n\n\n\n\nSTATS\n\n")

for elem in historicalList:
    print(elem)
    for ele in historicalList[elem]:
        print(ele)


print(historicalList)