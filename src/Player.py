import random

class Player():

    def __init__(self, name, symbole, epsilon=0.1):
        self.name = name
        self.symbole = symbole
        self.epsilon = epsilon

    def play(self, table):
        action = random.choice([i for i in range(9) if table[i] == '.'])
        table[action] = self.symbole
        return table, action
    
    def getName(self):
        return self.name