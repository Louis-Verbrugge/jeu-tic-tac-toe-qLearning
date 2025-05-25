import random
import numpy as np



class Player():

    def __init__(self, name, symbole, robot, epsilon=0.05, min_epsilon=0, decay_rate=0.99):
        self.name = name
        self.symbole = symbole
        self.robot = robot
        self.epsilon = epsilon
        self.win = -1  # -1 game pas fini | 0 game perdu | 1 game gagné
        self.decay_rate = decay_rate
        self.min_epsilon = min_epsilon



    def decay_epsilon(self):
        self.epsilon = max(self.min_epsilon, self.epsilon * self.decay_rate)


    def play(self, Q, table, learn, realPlayer=False):
        
        if self.robot:

            randomSearch = random.uniform(0, 1) < self.epsilon

            if randomSearch and learn:
                action = random.choice([i for i in range(9) if table[i] == '.'])
            else:
                # Exploitation : Choisir l'action ayant la meilleure Q-valeur
                state_str = convertTableToStr(table)
                if state_str not in Q:
                    Q[state_str] = [0] * 9  # Initialisation des Q-valeurs pour cet état si elles n'existent pas
                action = np.argmax(Q[state_str])  # Trouver l'action avec la plus grande Q-valeur


                while table[action] != '.':
                    # Si la case est occupée, choisir une nouvelle case vide
                    if randomSearch and learn:
                        action = random.choice([i for i in range(9) if table[i] == '.'])
                    else:
                        Q[convertTableToStr(table)][action] += -20 # punir l'action si c'est une case occupée
                        action = np.argmax(Q[convertTableToStr(table)])

            if learn:
                self.decay_epsilon()


        else:

            if realPlayer:
                action = int(input("Choisissez un nombre entre 0 et 8: "))
                while table[action] != '.':
                    action = int(input("Cette case est déjà prise, choisissez une autre case: "))

            else:
                
                action = random.randint(0, 8)
                while table[action] != '.':
                    action = random.randint(0, 8)


        action = int(action)
        table[action] = self.symbole
        return table, action
    
    
    def getName(self):
        return self.name
    

    
    def getWin(self):
        return self.win
    
    def getSymbole(self):
        return self.symbole
    
    def getEpsilon(self):
        return self.epsilon
    
    def getRobot(self):
        return self.robot
    

def convertTableToStr(table):
    return ''.join(["0" if table[i]=="." else "1" if table[i] == "X" else "2" for i in range(len(table))])



