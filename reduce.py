#reduce feature
from functools import reduce
ex = [10,10,10,10]
res = reduce(lambda x, y: x * y, ex)
print(res)

