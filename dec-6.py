from utils import getTodayInputFile
import math

USE_TEST_INPUT = False

def getAnswersSum() -> int:
    inputMatrix = transformInput(getParsedInput())
    return sum([getRowAnswer(row) for row in inputMatrix])

def getAnswersSum2() -> int:
    inputMatrix = getParsedInput2()
    return sum([getRowAnswer(row) for row in inputMatrix])


def getParsedInput() -> list:
    res = []
    with getTodayInputFile(USE_TEST_INPUT) as file:
        for line in file:
            res.append(line.split())
    return res

def transformInput(matrix: list) -> list:
    res = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            char = matrix[j][i]
            if char.isnumeric():
                row.append(int(char))
            else:
                row.append(char)
        res.append(row)
    return res

def getRowAnswer(row: list) -> int:
    if row[-1] == '+':
        func = sum
    elif row[-1] == '*':
        func = math.prod
    return func(row[:-1])

def getParsedInput2() -> list:
    matrix = []
    row = []
    operator = ''
    foundOperator = False
    with getTodayInputFile(USE_TEST_INPUT) as file:
        lines = file.readlines()
        lineLen = len(lines[0])
        for col in range(lineLen - 2, -1, -1):
            number = ''
            for line in lines:
                char = line[col]
                if char.isspace():
                    continue
                if not char.isnumeric():
                    foundOperator = True
                    operator = char
                    break
                number += char
            if foundOperator:
                row.append(int(number))
                row.append(operator)
                matrix.append(row)
                row = []
                operator = ''
                foundOperator = False
                # skip the next iteration, continue might not be enough here. MIght need to decrease col
            else:
                if number:
                    row.append(int(number))
    return matrix

print(getAnswersSum())
print(getAnswersSum2())