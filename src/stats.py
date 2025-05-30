
import numpy as np

def historical(historicalList, robot, tableBefore, action, tableNow):

    tableNowShadowCopy = tableNow.copy()
    tableBeforeShadowCopy = tableBefore.copy()
    
    if historicalList.get(robot) is None:
        historicalList[robot] = [(tableBeforeShadowCopy, action, tableNowShadowCopy)]
    else:
        historicalList[robot].append((tableBeforeShadowCopy, action, tableNowShadowCopy))

    return historicalList



def update_Q_table(Q, historicalList, robotWin, egality):
    alpha = 0.1
    gamma = 0.8
    reward_win = 10000
    reward_lose = -100000
    reward_egality = 10000


    for robot, action in historicalList.items():

      

        reward = reward_egality if egality else reward_win if robot == robotWin else reward_lose

    
        
        s = convertTableToStr(action[-1][0])
        a = action[-1][1]
        s_next = convertTableToStr(action[-1][2])


        if s not in Q:
            Q[s] = np.zeros(9)  # 9 actions possibles

        if s_next not in Q:
            Q[s_next] = np.zeros(9)


        Q[s][a] = Q[s][a] + alpha * (reward + gamma * np.max(Q[s_next]) - Q[s][a])



def convertTableToStr(table):
    return ''.join(["0" if table[i]=="." else "1" if table[i] == "X" else "2" for i in range(len(table))])




