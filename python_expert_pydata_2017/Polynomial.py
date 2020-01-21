# some behaviour that I want to implement -> write some (dunder) __ function __
# top-level function or top-level syntax -> corresponding __
# x + y     -> __add__
# init(x)   -> __init__
# repr(x)   -> __repr__
# x()       -> __call__
# https://docs.python.org/3/reference/datamodel.html?highlight=data%20model


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"{self.__class__.__name__} *({self.coeffs})"

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self, *args, **kwargs):
        pass


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)
