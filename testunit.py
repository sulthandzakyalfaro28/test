def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
