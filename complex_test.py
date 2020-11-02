from math import sqrt
from numbers import Real
import matplotlib.pyplot as plt


def alg(x, y):
    return f"{x} + i{y}"


class Complex:
    def __init__(self, a: float, b: float):
        """
        Example
        -------
        >>> z = Complex(1, 2)
        >>> print(z.a)
        1.0
        >>> print(z.b)
        2.0
        """
        self.a: Real = a
        self.b: Real = b

    def __add__(self, nb) -> "Complex":
        return Complex(self.a + nb.a, self.b + nb.b)

    def __sub__(self, nb) -> "Complex":
        return Complex(self.a - nb.a, self.b - nb.b)

    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return Complex(self.a * other.a + self.b * other.b, self.b * other.a - self.a * other.b)/self.module()
        elif isinstance(other, Real):
            return Complex(self.a/other, self.b/other)
        else:
            raise NotImplementedError

    def __mul__(self, nb) -> "Complex":
        return Complex(self.a * nb.a + self.b * nb.b, self.a * nb.a - self.b * nb.b)

    def __neg__(self) -> "Complex":
        return Complex(-self.a, -self.b)

    def __abs__(self):
        return self.module()

    def __copy__(self) -> "Complex":
        return Complex(self.a, self.b)

    def module(self) -> float:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.module())
        2.23606797749979
        """
        return sqrt(self.a ** 2 + self.b ** 2)

    def argument(self) -> tuple:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.argument())
        0.4472135954999579, 0.8944271909999159
        """
        return self.a / self.module(), self.b / self.module()
    
    def argument_write(self) -> str:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.argument_write())
        cos(theta) = 0.4472135954999579, sin(theta) = 0.8944271909999159
        """
        theta1 = self.a / self.module()
        theta2 = self.b / self.module()
        return f"cos(theta) = {theta1}, sin(theta) = {theta2}"

    def conjugate(self) -> "Complex":
        return Complex(self.a, -self.b)
    
    def conjug_write(self) -> str:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.conjugate())
        1 - 2i
        """
        if self.b - 0:
            sign = "-"
        else:
            sign = "+"
        return f"{self.a} {sign} {self.b}i"

    def real_pur(self) -> bool:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.real_pur())
        False
        >>> z2 = Complex(a=1)
        >>> print(z2.real_pur())
        True
        """
        if self.b == 0:
            return True
        else:
            return False

    def img_pur(self) -> bool:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.img_pur())
        False
        >>> z2 = Complex(b=2)
        >>> print(z2.img_pur())
        True
        """
        if self.a == 0:
            return True
        else :
            return False
        
    def pur(self):
        """
        Examples
        --------
        >>> z1 = Complex(a=1)
        >>> print(z1.pur())
        1 is a pur real.
        >>> z2 = Complex(b=2)
        >>> print(z2.img_pur())
        2i is a pur imaginary.
        """
        if self.real_pur():
            return f"{self.a} is a pur real."
        elif self.img_pur():
            return f"{self.b}i is a pur imaginary."
        else:
            return NotImplementedError

    def alg_write(self) -> str:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.alg_write())
        1 + 2i
        """
        return f"{self.a} + i{self.b}"

    def trigo_write(self) -> str:
        """
        Examples
        --------
        >>> z1 = Complex(1, 2)
        >>> print(z1.trigo_write())
        2.23606797749979 * cos(0.4472135954999579) + isin(0.8944271909999159)
        """
        arg = self.argument()
        return f"{self.module()} * cos({arg[0]}) + isin({arg[1]})"

    def trigonometric_circle_draw(self):
        plt.figure()
        plt.grid(True, linestyle='--')

        ax = plt.gca()
        ax.grid(True)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')

        max_lim: float = (self.a + self.b) + 5
        min_lim: float = -(self.a + self.b) - 5
        plt.xlim(min_lim, max_lim)
        plt.ylim(min_lim, max_lim)

        plt.scatter(self.a, self.b, color='red')
        plt.plot([0.0, self.a], [0.0, self.b], 'r-')
        circle1 = plt.Circle((0, 0), self.module(), color='b', fill=False)

        ax.add_artist(circle1)

        # title and label the axes
        plt.title("Some complex numbers")
        plt.xlabel("Real")
        plt.ylabel("Img")

        plt.show()

    __deepcopy__ = __copy__  # copy all the attribute


if __name__ == '__main__':
    z = Complex(10, 5)
    print(z.trigonometric_circle_draw())

