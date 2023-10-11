from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


now = time.time()
[fib(n) for n in range(32)]
[fib(n) for n in range(32)]
print(time.time() - now)
# print(fib.cache_info())