from utils import timer, getTodayInputFile

USE_TEST_INPUT = False

def main():
    print(getMaxJoltsSum())

@timer
def getMaxJoltsSum():
    results = []
    with getTodayInputFile(USE_TEST_INPUT, 3) as file:
        for line in file:
            # remove annoying newline character
            results.append(getMaxJolts2(line.strip()))
    return sum(results)

def getMaxJolts(line: str) -> int:
    currMax = 0
    for digit in line[:-1]:
        # see a digit
        # compare it to what would happen if we replaced the ones digit with it
        # compared what would happen if we replaced the tens digit with it and then just made the ones digit 1
        digitInOnes = replaceOnesDigit(currMax, int(digit))
        digitInTens = int(digit) * 10
        currMax = max(digitInOnes, digitInTens, currMax)
    currMax = max(currMax, replaceOnesDigit(currMax, int(line[-1])))
    return currMax

def getMaxJolts2(line:str) -> int:
    resList = ['0'] * 12
    for i, digit in enumerate(line):
        # when there are 12 left, we want this to be 0, then increase until it's at 12.
        startComparison = max(i + 12 - (len(line)), 0)
        for j in range(startComparison, 12):
            if int(digit) > int(resList[j]):
                resList[j] = digit
                #reset the rest of the resList(if applicable) to 0s
                resList[j+1:12] = ['0'] * (12 - (j + 1))
                break
    return int(''.join(resList))

def replaceOnesDigit(num: int, ones: int) -> int:
    return ((num // 10) * 10) + ones

main()