def addition(a,b):
    return a+b
def soustration(a,b):
    return a-b
def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        raise ValueError('impossible de diviser par 0')
    return a/b