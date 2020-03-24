from rational_numbers import find_greatest_common_denominator 
from rational_numbers import Rational


def gcd(a, b):

	def inner_gcd(a, b):
		if a == b :
			return a
		elif a > b :
			return inner_gcd(a - b, b)
		else :
			return inner_gcd(a, b - a)

	if a == 0 or b == 0 :
		return 1

	a = abs(a)
	b = abs(b)

	return inner_gcd(a, b)

	

print("hello")

#r = Rational(1, 2) + Rational(-1, 2)
#print(r)



#a = -18
#b = -48

a = 0
b = 4
print(find_greatest_common_denominator(a, b))



