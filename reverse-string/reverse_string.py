def reverse(text):
	#my solution (could be better)
	return ''.join([text[x] for x in range(len(text) - 1, -1, -1)])

	#Community favourite and simplest solution
	#return text[::-1]

