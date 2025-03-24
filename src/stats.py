
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
    reward_win = 10
    reward_lose = -10


    for robot, action in historicalList.items():

        if egality:
            pass

        reward = 0 if egality else reward_win if robot == robotWin else reward_lose

        for elem in action:


            # print(elem)
            # print("\n\n")
            # print(f"{elem[0]} + \n + {elem[1]} + \n + {elem[2]}")
            
            s = convertTableToStr(elem[0])
            a = elem[1]
            s_next = convertTableToStr(elem[2])


            # print(f"s: {s}, type: {type(s)}")
            # print(f"s_next: {s_next}, type: {type(s_next)}")

            if s not in Q:
                Q[s] = np.zeros(9)  # 9 actions possibles

            if s_next not in Q:
                Q[s_next] = np.zeros(9)


            Q[s][a] = int(Q[s][a] + alpha * (reward + gamma * np.max(Q[s_next]) - Q[s][a]))


def convertTableToStr(table):
    return ''.join(["0" if table[i]=="." else "1" if table[i] == "X" else "2" for i in range(len(table))])




