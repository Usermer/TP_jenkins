"""Module de calculs simples : addition, soustraction, multiplication, division."""


def addition(a, b):
    """Retourne la somme de a et b."""
    return a + b


def soustraction(a, b):
    """Retourne la différence entre a et b."""
    return a - b


def multiplication(a, b):
    """Retourne le produit de a et b."""
    return a * b


def division(a, b):
    """Retourne le quotient de a par b."""
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b