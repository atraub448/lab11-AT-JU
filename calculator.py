import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b

def logarithm(a, b):
    # log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Invalid logarithm base")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b


