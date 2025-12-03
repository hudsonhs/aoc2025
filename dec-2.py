from time import time
from concurrent.futures import ProcessPoolExecutor

def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def main():
    file = open('inputs/dec-2-1')
    rawInput = file.read()
    intervals = rawInput.split(',')
    print(getAllRangesSum(intervals))
    print(getAllRangesSumsInParallel(intervals))
    print(getEachRangeSumInParallel(intervals))

@timer_func
def getAllRangesSum(ranges: list) -> int:
    res = 0
    for range in ranges:
        res += getRangeSum(range)
    return res

@timer_func
def getAllRangesSumsInParallel(ranges: list) -> int:
    with ProcessPoolExecutor() as executor:
        invalidIdsInRanges = executor.map(getRangeSum, ranges)
    return sum(invalidIdsInRanges)

@timer_func
def getEachRangeSumInParallel(ranges:list) -> int:
    res = 0
    for range in ranges:
        res += getRangeSumInParallel(range)
    return res

def getRangeSum(interval: str) -> int:
    res = 0
    intervalMin, intervalMax = interval.split('-')
    intervalMin, intervalMax = int(intervalMin), int(intervalMax)
    # we should be able to parallelize the below since it's just addition
    for x in range(intervalMin, intervalMax+1):
        if isInvalid(x):
            res += x
    return res

def getRangeSumInParallel(interval: str) -> int:
    intervalMin, intervalMax = interval.split('-')
    intervalMin, intervalMax = int(intervalMin), int(intervalMax)
    # we should be able to parallelize the below since it's just addition
    with ProcessPoolExecutor() as executor:
        invalidNums = executor.map(numIfInvalid, range(intervalMin, intervalMax + 1))
    return sum(invalidNums)

def numIfInvalid(n: int) -> int:
    return n if isInvalid(n) else 0

def isInvalid(n: int) -> bool:
    if n < 11:
        return False
    numAsString = str(n)
    # make a sliding window and iterate over the whole string based on how large the window is
    for patternSize in range(1, (len(numAsString) // 2) + 1):
        if len(numAsString) % patternSize != 0:
            continue
        l = 0
        r = patternSize
        pattern = numAsString[:patternSize]
        while r <= len(numAsString):
            if numAsString[l:r] == pattern:
                l += patternSize
                r += patternSize
            else:
                break
        if l == len(numAsString):
            return True
    return False

if __name__ == '__main__':
    main()