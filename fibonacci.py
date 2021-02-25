def fibonacci(value):
    if is_int(value) and value >= 0:
        return fibonacci_rec(value)
    else:
        return None


def fibonacci_rec(value):
    if value == 0 or value == 1:
        return value
    else:
        return fibonacci_rec(value - 1) + fibonacci_rec(value - 2)


def factorial(value):
    if is_int(value) and value >= 0:
        return factorial_rec(value)
    else:
        return None


def factorial_rec(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * factorial_rec(value - 1)


def is_int(value):
    if isinstance(value, int):
        return True
    else:
        return False
