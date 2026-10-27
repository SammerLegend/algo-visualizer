def run(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1
