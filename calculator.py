def addition(a, b):
    result = a + b
    return result

def substraction(a, b):
    result = a - b
    return result

def division(a, b):
    if b == 0:
        print("Erreur : Division par zéro")
        return None
    else:
        result = a / b
        return result