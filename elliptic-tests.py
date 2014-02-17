from elliptic import *
from fractions import Fraction as frac

C = EllipticCurve(a=frac(-2), b=frac(4))
P = Point(C, frac(3), frac(5))
Q = Point(C, frac(-2), frac(0))
zero = Ideal(C)

P + Q
Q + P
5*P
Q - 3*P

