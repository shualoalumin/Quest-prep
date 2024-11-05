from functools import reduce

n = [i for i in range(1,101)]

reduce(lambda x, y : x+y, n)
