def run(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative integers.")
    if n in (0, 1):
        return n
    return run(n - 1) + run(n - 2)
