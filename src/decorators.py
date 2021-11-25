def checkPositive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Value must be positive")
        return func(x)
    return wrapper