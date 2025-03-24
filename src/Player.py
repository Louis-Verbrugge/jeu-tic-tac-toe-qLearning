import random
import numpy as np



class Player():

    def __init__(self, name, symbole, robot, epsilon=0.1):
        self.name = name
        self.symbole = symbole
        self.robot = robot
        self.epsilon = epsilon
        self.win = -1  # -1 game pas fini | 0 game perdu | 1 game gagné

    def play(self, Q, table, learn):

        if self.robot:

            if random.uniform(0, 1) < self.epsilon and learn:
                action = random.choice([i for i in range(9) if table[i] == '.'])
            else:
                # Exploitation : Choisir l'action ayant la meilleure Q-valeur
                state_str = convertTableToStr(table)
                if state_str not in Q:
                    Q[state_str] = [0] * 9  # Initialisation des Q-valeurs pour cet état si elles n'existent pas
                action = np.argmax(Q[state_str])  # Trouver l'action avec la plus grande Q-valeur


                while table[action] != '.':
                    # Si la case est occupée, choisir une nouvelle case vide
                    if random.uniform(0, 1) < self.epsilon and learn:
                        action = random.choice([i for i in range(9) if table[i] == '.'])
                    else:
                        action = np.argmax(Q[convertTableToStr(table)])

        else:
            action = int(input("dit un nombre entre 0 et 8: "))

            while table[action] != '.':
                action = int(input("tu dois choisir une autre case car elle est déjà prise: "))


        action = int(action)
        table[action] = self.symbole
        return table, action
    
    
    def getName(self):
        return self.name
    

    
    def getWin(self):
        return self.win
    

def convertTableToStr(table):
    return ''.join(["0" if table[i]=="." else "1" if table[i] == "X" else "2" for i in range(len(table))])



