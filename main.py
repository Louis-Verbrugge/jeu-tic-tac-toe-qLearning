

import numpy as np

from src.Player import Player
from src.stats import historical, update_Q_table


NOMBRE_ENTRAINEMENT = 1_000_001


def endGame(table):
    # return true if end game and the second bool is for egality or win

    return '.' not in table or \
        table[0] == table[1] == table[2] != '.' or \
        table[3] == table[4] == table[5] != '.' or \
        table[6] == table[7] == table[8] != '.' or \
        table[0] == table[3] == table[6] != '.' or \
        table[1] == table[4] == table[7] != '.' or \
        table[2] == table[5] == table[8] != '.' or \
        table[0] == table[4] == table[8] != '.' or \
        table[2] == table[4] == table[6] != '.', '.' not in table
        


def displayTable(table):

    print("\n\n")
    for i in range(len(table)):
        if i%3==0:
            print('')
        print(table[i], end='')


    print("\n")
Q = {} 


def main(learn = True):

    for nombreGame in range (NOMBRE_ENTRAINEMENT if learn else 20):

        historicalList={}
        table = ['.']*9
        player1 = Player('Joueur 1', 'X', True)

        if learn:
            player2 = Player('Joueur 2', 'O', True)
            
        else:
            player2 = Player('Joueur 2', 'O', False)


        playerList = (player1, player2)

        runGame = False

        while not runGame:

            tableBefore = table.copy()
            table, action = playerList[0].play(Q, table, learn)

            historicalList = historical(historicalList, playerList[0].getName(), tableBefore, action, table)
            
            if not learn:
                displayTable(table)

            playerList = tuple(reversed(playerList))

            runGame, egality = endGame(table)



        if learn:
            update_Q_table(Q, historicalList, playerList[1].name, egality)

            

            stats = {} 
            for elem in historicalList:

                win = 1 if elem == playerList[0].getName() else 0
                
                for ele in historicalList[elem]:
                    if stats.get((str(ele[0]), str(ele[1]))) != None:
                        stats[str(ele[0])].append(win)
                    else:
                        stats[str(ele[0])] = [win]
                        
                    
            if nombreGame % 10000 == 0:
                print(f"games: {nombreGame}")
            # print(stats)

        else:
            print(f"Le gagant et: {playerList[1].name if '.' in table else "EGALITE"}")



#entrainement IA:
main()

#joueur joue avec le robot:
main(False)
