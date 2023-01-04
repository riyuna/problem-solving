def powerset(array):
	if len(array) == 1:
		return [0, array[0]]
	
	previous = powerset(array[:-1])
	previous.extend([v + array[-1] for v in previous])

	return previous


def make_case(array):
	ps = powerset(array)
	__import__("random").shuffle(ps)

	print(len(array))
	for v in ps:
		print(v)


if __name__ == "__main__":
	array = [1, 3, 0, -2, -2, 4]
	result_array = [-4, 0, 1, 2, 2, 3]

	if True:
		print(sorted(powerset(array)) == sorted(powerset(result_array)))
	else:
		make_case(array)
