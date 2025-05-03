def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b


def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print("denominator cant be 0")