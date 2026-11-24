import pytest
from calculator import addition, soustraction, division, multiplication


def test_addition():
    assert addition(2, 3) == 5


def test_soustraction():
    assert soustraction(3, 2) == 1


def test_multiplication():
    assert multiplication(3, 2) == 6


def test_division():
    assert division(6, 2) == 3