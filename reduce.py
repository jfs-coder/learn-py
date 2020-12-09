#reduce feature
from functools import reduce
ex = [10,10,10,10]
res = reduce(lambda x, y: x * y, ex)
print(res)

ex2 = [6,3,7,4,6]

res = reduce(lambda x, y: x - y, ex2)
print(res)

