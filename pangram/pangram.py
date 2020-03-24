import string  

def is_pangram(sentence):
# Ver 2 - Updated
	if not sentence:
		return False

	return set(string.ascii_lowercase) <= set(sentence.casefold())

# Ver 1 - original
	sentence = sentence.strip().lower()
	alphabetLength = len(string.ascii_lowercase)

	accumulator = ''

	for c in sentence :
		if c.isalpha() and c not in accumulator :
			accumulator += c
			#print('%s added to accumulator: "%s" length: %i' % (c, accumulator, len(accumulator)))

	if len(accumulator) == alphabetLength :
		return True

	return False


