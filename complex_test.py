from math import sqrt, tan
from numbers import Real


class Complex:
    def __init__(self, a: Real, b: Real):
        self.a: Real = a
        self.b: Real = b

    def __add__(self, nb):
        return Complex(self.a + nb.a, self.b + nb.b)

    def __sub__(self, nb):
        return Complex(self.a - nb.a, self.b - nb.b)

    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return Complex(self.a * other.a + self.b * other.b, self.b * other.a - self.a * other.b)/self.module()
        elif isinstance(other, Real):
            return Complex(self.a/other, self.b/other)
        # elif isinstance(other, complex):
        #     ...
        else:
            raise NotImplementedError

    def __mul__(self, nb):
        return Complex(self.a * nb.a + self.b * nb.b, self.a * nb.a - self.b * nb.b)

    def __neg__(self):
        return Complex(-self.a, -self.b)

    def __abs__(self):
        return self.module()

    def __copy__(self) -> "Complex":
        return Complex(self.a, self.b)

    def module(self) -> Real:
        return sqrt(self.a ** 2 + self.b ** 2)

    def argument(self) -> Real:
        return tan(self.b / self.a)

    def conjug(self):
        ...

    def real_pur(self) -> bool:
        if self.b == 0:
            return True
        else:
            return False

    def img_pur(self) -> bool:
        if self.a == 0:
            return True
        else :
            return False

    def pur(self):
        if self.real_pur():
            print("It's a pur real.")
        elif self.img_pur():
            print("It's a pur imaginary.")
        else:
            print("Error.")

    def expo(self):
        print(self.module(), "e^(ĵ", self.argument(), ")")

    def alg(self):
        print(self.a, "+ i", self.b)

    __deepcopy__ = __copy__  # copy all the attribute
