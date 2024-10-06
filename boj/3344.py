n=int(input())
if n%6 not in (2, 3):
	for i in range(2, n+1, 2):print(i)
	for i in range(1, n+2, 2):print(i)
else:
	if n%6==2:
		for i in range(2, n+1, 2):print(i)
		print(3)
		print(1)
		for i in range(7, n+1, 2):print(i)
		print(5)
	else:
		for i in range(4, n+1, 2):print(i)
		print(2)
		for i in range(5, n+1, 2):print(i)
		print(1)
		print(3)