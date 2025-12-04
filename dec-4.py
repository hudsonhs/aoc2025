def getNumRemovableRolls():
    rolls = serializeRolls('inputs/dec-4')
    prevRemovableRolls = set()
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
    with open(path) as file:
        for line in file:
            rolls.append(list(line.strip()))
    return rolls

def getAccessibleRolls(rolls: list) -> set:
    res = set()
    for y in range(len(rolls)):
        for x in range(len(rolls[0])):
            if rolls[y][x] == '@' and isRollAccessible(y, x, rolls):
                res.add((y, x))
    return res

def isRollAccessible(y: int, x: int, rolls: list) -> bool:
    adjRolls = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            checkY = y + dy
            checkX = x + dx
            if 0 <= checkY < len(rolls) and 0 <= checkX < len(rolls[0]) and rolls[checkY][checkX] == '@':
                adjRolls += 1
                if adjRolls > 3:
                    return False
    return True

def removeRolls(rolls: list, rollsToRemove: set) -> None:
    for y, x in rollsToRemove:
        rolls[y][x] = '.'

print(getNumRemovableRolls())
