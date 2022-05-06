import doctest


def sum(x, y):
    """ sum x e y

    >>> sum(10, 20)
    30

    >>> sum(-10, 20)
    10

    >>> sum('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'

    return x + y


def subtract(x, y):
    """ sum x e y

    >>> subtract(10, 5)
    5

    >>> subtract(50, 20)
    30

    >>> subtract('50', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'

    return x - y


if __name__ == '__main__':
    doctest.testmod(verbose=True)
