def run(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number in (0, 1):
        return 1
    return number * run(number - 1)
