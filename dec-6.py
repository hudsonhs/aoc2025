from utils import getTodayInputFile
import math

USE_TEST_INPUT = False

def getAnswersSum() -> int:
    inputMatrix = getParsedInput()
    return sum([getRowAnswer(row) for row in inputMatrix])

def getAnswersSum2() -> int:
    inputMatrix = parseZippedInput(zippedStringInput())
    return sum([getRowAnswer(row) for row in inputMatrix])


def getParsedInput() -> list:
    res = []
    with getTodayInputFile(USE_TEST_INPUT) as file:
        for line in file:
            res.append(line.split())
    return list(zip(*res))

def getRowAnswer(row: list) -> int:
    if row[-1] == '+':
        func = sum
    elif row[-1] == '*':
        func = math.prod
    return func([int(num) for num in row[:-1]])

def zippedStringInput() -> list:
    with getTodayInputFile(USE_TEST_INPUT) as file:
        lines = file.readlines()
    separatedInputs = [''.join(tup).strip() for tup in list(zip(*lines))]
    return separatedInputs

def parseZippedInput(strList: list) -> list:
    matrix = []
    currOperator = ''
    row = []
    for s in strList:
        if currOperator == '':
            currOperator = s[-1]
            row.append(int(s[:-1]))
        elif s == '':
            row.append(currOperator)
            matrix.append(row)
            row = []
            currOperator = ''
        else:
            row.append(int(s))
    return matrix

def getParsedInput2() -> list:
    matrix = []
    row = []
    operator = ''
    foundOperator = False
    with getTodayInputFile(USE_TEST_INPUT) as file:
        lines = file.readlines()
        lineLen = len(lines[0])
        for col in range(lineLen - 2, -1, -1):
            number = 0
            for line in lines:
                char = line[col]
                if char.isspace():
                    continue
                if not char.isnumeric():
                    foundOperator = True
                    operator = char
                    break
                number = (number * 10) + int(char)
            if foundOperator:
                row.append(number)
                row.append(operator)
                matrix.append(row)
                row = []
                operator = ''
                foundOperator = False
            else:
                if number != 0:
                    row.append(number)
    return matrix

print(getAnswersSum())
print(getAnswersSum2())
