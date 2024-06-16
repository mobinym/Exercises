# test_um.py
import pytest
import um

def test_count():
    assert um.count('um') == 1
    assert um.count('um?') == 1
    assert um.count('Um, thanks for the album.') == 1
    assert um.count('Um, thanks, um...') == 2
    assert um.count('yummy') == 0

if __name__ == "__main__":
    pytest.main()
