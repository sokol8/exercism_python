import math

def is_armstrong(number) -> bool:
	count = int(math.log10(abs(number))+1)
	accumulator = 0
	numberCopy = number

	while 0 < numberCopy:
		digit = numberCopy % 10
		accumulator += digit ** count
		numberCopy //= 10

	return accumulator == number

