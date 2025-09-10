import questions.python.app as app

def test_add_numbers():
    assert app.add_numbers(2, 3) == 5
    assert app.add_numbers(-1, 1) == 0
    assert app.add_numbers(0, 0) == 0
