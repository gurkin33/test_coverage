from something import Something


def test_something_get_true():
    assert Something.get_true()


def test_something_get_false():
    assert Something.get_false() is False


def test_something_get_1():
    assert Something.get_1() == 1


def test_something_get_2():
    assert Something.get_2() == 2
