from src.addition import add_numbers

def test_add_numbers():
    assert add_numbers(1, 0) == 1
    assert add_numbers(3, -1) == 2