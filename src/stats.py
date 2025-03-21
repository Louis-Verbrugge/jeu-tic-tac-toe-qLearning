
def historical(historicalList, robot, tableBefore, action, tableNow):

    tableNowShadowCopy = tableNow.copy()
    tableBeforeShadowCopy = tableBefore.copy()
    
    if historicalList.get(robot) is None:
        historicalList[robot] = [(tableBeforeShadowCopy, action, tableNowShadowCopy)]
    else:
        historicalList[robot].append((tableBeforeShadowCopy, action, tableNowShadowCopy))

    return historicalList