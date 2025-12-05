from utils import getTodayInputFile

USE_TEST_INPUT = False

def getNumIngredientsInRanges():
    res = 0
    ranges = getRanges()
    ingredients = getIngredients()
    for ingredient in ingredients:
        for range in mergeIntervals(ranges):
            if isInInterval(ingredient, range):
                res += 1
    return res

def getNumFreshIngredients():
    res = 0
    intervals = mergeIntervals(getRanges())
    for interval in intervals:
        res += (interval[1] - interval[0]) + 1
    return res

def getRanges() -> list:
    ranges = []
    with getTodayInputFile(USE_TEST_INPUT) as file:
        for line in file:
            if line == '\n':
                break
            ranges.append([int(line.split('-')[0]), int(line.split('-')[1])])
    return ranges

def getIngredients() -> list:
    ingredients = []
    with getTodayInputFile(USE_TEST_INPUT) as file:
        startCollectingIngredients = False
        for line in file:
            if startCollectingIngredients:
                ingredients.append(int(line))
            if line == '\n':
                startCollectingIngredients = True
    return ingredients

def mergeIntervals(intervals: list) -> list:
    intervals.sort(key=lambda x: x[0])
    merged = []
    currInterval = intervals[0]
    for potentialInterval in intervals[1:]:
        if potentialInterval[0] <= currInterval[1]:
            currInterval[1] = max(potentialInterval[1], currInterval[1])
        else:
            merged.append(currInterval.copy())
            currInterval = potentialInterval
    merged.append(currInterval)
    return merged


def isInInterval(num: int, interval: list):
    return interval[0] <= num <= interval[1]

print(getNumIngredientsInRanges())
print(getNumFreshIngredients())

# Make your own little edge cases in the smaller testing input
