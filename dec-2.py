from utils import timer, getTodayInputFile
from concurrent.futures import ProcessPoolExecutor

USE_TEST_INPUT = False

def main():
    with getTodayInputFile(USE_TEST_INPUT, 2) as file:
        rawInput = file.read()
    ranges = rawInput.split(',')
    print(getAllRangeSumsInParallel(ranges))

@timer
def getAllRangeSumsInParallel(ranges: list) -> int:
    with ProcessPoolExecutor() as executor:
        invalidIdsInRanges = executor.map(getRangeSum, ranges)
    return sum(invalidIdsInRanges)

def getRangeSum(range_str: str) -> int:
    res = 0
    rangeMin, rangeMax = range_str.split('-')
    rangeMin, rangeMax = int(rangeMin), int(rangeMax)
    # Each call to isInvalid is so fast that parallelizing without chunking doesn't speed this up
    for x in range(rangeMin, rangeMax + 1):
        if isInvalid(x):
            res += x
    return res

def isInvalid(n: int) -> bool:
    if n < 11:
        return False
    numAsString = str(n)
    for patternSize in range(1, (len(numAsString) // 2) + 1):
        if len(numAsString) % patternSize != 0:
            continue
        pattern = numAsString[:patternSize]
        if numAsString == pattern * (len(numAsString) // patternSize):
            return True
    return False

if __name__ == '__main__':
    main()
