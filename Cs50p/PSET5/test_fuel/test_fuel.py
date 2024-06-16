# test_fuel.py
import pytest
import fuel

def test_convert():
    assert fuel.convert('50/100') == 50
    with pytest.raises(ValueError):
        fuel.convert('101/100')
    with pytest.raises(ZeroDivisionError):
        fuel.convert('1/0')
    with pytest.raises(ValueError):
        fuel.convert('a/b')

def test_gauge():
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(50) == '50%'

if __name__ == "__main__":
    pytest.main()
