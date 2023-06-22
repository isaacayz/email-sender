from functools import lru_cache
from datetime import datetime

start_time = datetime.now()
#@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n -2)

a=fibonacci(15)
b=fibonacci(25)
print(f"Fibonacci of 15 is {a}, of 25 is {b}")

end_time = datetime.now()
total = (end_time - start_time).total_seconds() * 10**3
print(f"The total time taken for the execution is {total:.3f}")