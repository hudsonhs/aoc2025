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
    print(getAllRangesSumsInParallel(intervals))

@timer_func
def getAllRangesSumsInParallel(ranges: list) -> int:
    with ProcessPoolExecutor() as executor:
        invalidIdsInRanges = executor.map(getRangeSum, ranges)
    return sum(invalidIdsInRanges)

def getRangeSum(interval: str) -> int:
    res = 0
    intervalMin, intervalMax = interval.split('-')
    intervalMin, intervalMax = int(intervalMin), int(intervalMax)
    # Each call to isInvalid is so fast that parallelizing without chunking doesn't speed this up
    for x in range(intervalMin, intervalMax+1):
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
        if numAsString == pattern * (len(numAsString)//patternSize):
            return True
    return False

if __name__ == '__main__':
    main()
