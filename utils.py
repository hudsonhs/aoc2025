from time import time
from pathlib import Path
from datetime import date

def timer(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def getTodayInputFile(test: bool):
    testStr = '-test' if test else ''
    return Path(f'./inputs/dec-{date.today().day}{testStr}').open()
