# -*- coding: utf-8 -*-
# NEGORO Tetsuya, 2015-10
# utilitiy functions and classes


def type_check(*argtypes, **kwargtypes):
    import functools

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for t, arg in zip(argtypes, args):
                if not isinstance(arg, t):
                    raise TypeError
            for key, arg in kwargs.items():
                t = kwargtypes[key]
                if not isinstance(arg, t):
                    raise TypeError
            return f(*args, **kwargs)
        return wrapper
    return decorator


class UniterableString(str):

    """String does not implements __iter__ method
    to prevent dealt as Iterable
    """
    def __new__(cls, *args, **kwargs):
        return str.__new__(cls, *args, **kwargs)

    def __iter__(self):
        raise TypeError
