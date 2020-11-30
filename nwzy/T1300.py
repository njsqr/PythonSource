"""
@author
"""
"""
def fun(n):
    res = fun.cache.get(n, None)
    if res:
        return res

    res = []
    for step in (1, 2):
        if n < step: break
        for p in fun(n - step):
            res.append([step] + p)

    fun.cache[n] = res
    return res
fun.cache = {0:[[]]}
"""


def fun(n, a, x, y, z):
    a[0] = 1
    for i in range(n):
        a[i + x] += a[i]
        a[i + y] += a[i]
        a[i + z] += a[i]
    return a[n]


n = int(input())
up = [0] * (n + 5)
down = [0] * (n + 5)

print(fun(n, up, 1, 2, 3))