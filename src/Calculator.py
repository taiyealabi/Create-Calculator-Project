def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    return int(a) * int(b)

def division(a, b):
    a = int(a)
    b = int(b)
    return int(a) / int(b)

def sq(a):
    a = int(a)
    return int(a) * int(a)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

