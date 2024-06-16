import pytest
import bank

def test_value_hello():
    assert bank.value('Hello') == 0

def test_value_h():
    assert bank.value('Hi') == 20

def test_value_other():
    assert bank.value('Good morning') == 100

def test_value_empty():
    assert bank.value('') == 100
