def getNumRemovableRolls():
    rolls = serializeRolls('inputs/dec-4')
    prevRemovableRolls = []
    res = 0
    currRemovableRolls = getAccessibleRolls(rolls)
    while prevRemovableRolls != currRemovableRolls:
        res += len(currRemovableRolls)
        removeRolls(rolls, currRemovableRolls)
        prevRemovableRolls = currRemovableRolls
        currRemovableRolls = getAccessibleRolls(rolls)
    return res

def serializeRolls(path: str) -> list:
    rolls = []
    file = open(path)
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        rolls.append(row.copy())
    return rolls

def getAccessibleRolls(rolls):
    res = []
    for y in range(len(rolls)):
        for x in range(len(rolls[0])):
            if rolls[y][x] == '@' and isRollAccessible(y, x, rolls):
                res.append((y, x))
    return res

def isRollAccessible(y: int, x: int, rolls: list) -> bool:
    adjRolls = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            checkY = y + dy
            checkX = x + dx
            if (not (dy == 0 and dx == 0)) and 0 <= checkY < len(rolls) and 0 <= checkX < len(rolls[0]) and rolls[checkY][checkX] == '@':
                adjRolls += 1
                if adjRolls > 3:
                    return False
    return True

def removeRolls(rolls: list, rollsToRemove: list) -> None:
    for y, x in rollsToRemove:
        rolls[y][x] = '.'

print(getNumRemovableRolls())
