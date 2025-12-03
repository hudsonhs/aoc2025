from time import time

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


@timer_func
def main():
    file = open('inputs/dec-2-1')
    rawInput = file.read()
    intervals = rawInput.split(',')
    print(getInvalidIdSum(intervals))

def getInvalidIdSum(intervals: list) -> int:
    res = 0
    for interval in intervals:
        # should be able to parallelize this since it's just addition
        res += getInvalidIdSumInRange(interval)
    return res

def getInvalidIdSumInRange(interval: str) -> int:
    res = 0
    intervalMin, intervalMax = interval.split('-')
    intervalMin, intervalMax = int(intervalMin), int(intervalMax)
    # we should be able to parallelize the below since it's just addition
    for x in range(intervalMin, intervalMax+1):
        if isInvalid(x):
            res += x
    return res

def isInvalid(n: int) -> bool:
    if n < 11:
        return False
    numAsString = str(n)
    # make a sliding window and iterate over the whole string based on how large the window is
    for patternSize in range(1, len(numAsString)//2 + 1):
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


main()