if __name__ == "__main__":
	is_add = True
	stk = []
	val = 0
	div = 10**9+7

	n = int(input())
	for v in input().split():
		if v == "(":
			if is_add:
				stk.append(val)
				val = 1
				is_add = False
			else:
				stk.append(val)
				val = 0
				is_add = True
		elif v == ")":
			if is_add:
				w = stk.pop()
				val *= w
				val %= div
				is_add = False
			else:
				w = stk.pop()
				val += w
				val %= div
				is_add = True
		else:
			if is_add:
				val += int(v)
			else:
				val *= int(v)
			val %= div
	
	print(val)
