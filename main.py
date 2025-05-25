

import numpy as np
import pickle
import os

from src.Player import Player
from src.stats import historical, update_Q_table


NOMBRE_ENTRAINEMENT = 100_001
NOMBRE_GAME_RANDOM = 50_001


def endGame(table):
    # return true if end game and the second bool is for egality or win

    win = table[0] == table[1] == table[2] != '.' or \
        table[3] == table[4] == table[5] != '.' or \
        table[6] == table[7] == table[8] != '.' or \
        table[0] == table[3] == table[6] != '.' or \
        table[1] == table[4] == table[7] != '.' or \
        table[2] == table[5] == table[8] != '.' or \
        table[0] == table[4] == table[8] != '.' or \
        table[2] == table[4] == table[6] != '.'
    
    return win, not win and '.' not in table
        


def displayTable(table):

    print("\n\n")
    for i in range(len(table)):
        if i%3==0:
            print('')
        print(table[i], end='')


    print("\n")



def main(learn = True):



    for nombreGame in range (NOMBRE_ENTRAINEMENT):

        historicalList={}
        table = ['.']*9
        player1 = Player('Joueur 1', 'X', True)

        if learn:
            player2 = Player('Joueur 2', 'O', True)
            
        else:
            player2 = Player('Joueur 2', 'O', False)


        playerList = (player1, player2)

        runGame = False
        egality = False

        while not runGame and not egality:

            tableBefore = table.copy()
            table, action = playerList[0].play(Q, table, learn)

            historicalList = historical(historicalList, playerList[0].getName(), tableBefore, action, table)

            playerList = tuple(reversed(playerList))

            runGame, egality = endGame(table)





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
       

    print("\n\n")
    print(f"Voici la valeur de episilon: {player1.getEpsilon()} et {player2.getEpsilon()}")



def evaluate_ai_performance():

    
    player1 = Player('Joueur 1', 'X', True)
    player2 = Player('Joueur 2', 'O', False)

    
 

    endWin = 0    
    endEgality = 0
    endLose = 0

    for _ in range(NOMBRE_GAME_RANDOM):

        table = ['.']*9
        runGame = False
        egality = False
        playerList = (player1, player2)


        while not runGame and not egality:

        
            table, _ = playerList[0].play(Q, table, False)
            playerList = tuple(reversed(playerList))
            runGame, egality = endGame(table)

    

        if egality:
            endEgality += 1
        elif playerList[1].getSymbole() == 'X':
            endWin += 1
        else:
            endLose += 1

    print("\n\n")
    print(f"Nombre de partie: {NOMBRE_GAME_RANDOM}")
    print(f"{round((endWin / NOMBRE_GAME_RANDOM) * 100, 2)}% de victoire")
    print(f"{round((endLose / NOMBRE_GAME_RANDOM) * 100, 2)}% de défaite")
    print(f"{round((endEgality / NOMBRE_GAME_RANDOM) * 100, 2)}% d'égalité")





Q = {} 

# Charger la Q-table si elle existe
if os.path.exists('Q_table.pkl'):
    with open('Q_table.pkl', 'rb') as f:
        Q = pickle.load(f)

# print("Début de l'entraînement...")
# main(True)
# main(False)

# Sauvegarder la Q-table après l'entraînement
with open('Q_table.pkl', 'wb') as f:
    pickle.dump(Q, f)

print("Entraînement terminé. Début de l'évaluation...")
evaluate_ai_performance()






