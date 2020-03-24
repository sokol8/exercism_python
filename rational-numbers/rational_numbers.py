from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.__normaliseSign__()
        self.__reduce__()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        r = Rational(
            (self.numer * other.denom + other.numer * self.denom), 
            (self.denom * other.denom))
        return r

    def __sub__(self, other):
        other.numer = -other.numer
        return self + other

    def __mul__(self, other):
        r = Rational(
            (self.numer * other.numer),
            (self.denom * other.denom))
        return r

    def __truediv__(self, other):
        inverted = other.invertedNumber()
        return self * inverted

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        r = Rational(
            (self.numer ** power), 
            (self.denom ** power))
        return r

    def __rpow__(self, base):
        return base ** self.floatValue()
        
    def floatValue(self):
        return self.numer / self.denom

    def __reduce__(self):
        gcdValue = Rational.find_greatest_common_denominator(self.numer, self.denom)
        self.numer /= gcdValue
        self.denom /= gcdValue

    def invertedNumber(self):
        numer = self.numer
        denom = self.denom
        return Rational(denom, numer)

    def __normaliseSign__(self):
        if self.denom < 0 and self.numer < 0:
            self.denom *= -1
        elif self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    @staticmethod
    def find_greatest_common_denominator(a, b):
        return abs(a) if (b == 0) else Rational.find_greatest_common_denominator(b, a % b)


