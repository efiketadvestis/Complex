from math import sqrt, tan
from numbers import Real
import matplotlib.pyplot as plt
import numpy as np


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

    def expo_write(self):
        print(self.module(), "e^(ĵ", self.argument(), ")")

    def alg_write(self):
        print(self.a, "+ i", self.b)

    def trigo_write(self):
        print(self.module(), "(cos(", self.argument(), ") + i*sin(", self.argument(), "))")

    def trigonometric_circle_draw(self):
        plt.figure()
        ax = plt.gca()

        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')

        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.grid(True, linestyle='--')

        plt.scatter(self.a, self.b, color='red', s=2)

        plt.show()

        # title and label the axes
        plt.title("Some complex numbers")
        plt.xlabel("Real")
        plt.ylabel("Img")

        plt.show()

    __deepcopy__ = __copy__  # copy all the attribute


if __name__ == '__main__':
    a = 1
    b = 2
    z = Complex(a, b)

