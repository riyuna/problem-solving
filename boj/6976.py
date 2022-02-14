for i in ' '*int(input()):
	n=int(input())
	orign=n
	while True:
		print(n)
		r=n%10
		n//=10
		n-=r
		if n<1:break
	if n==0:print(f'The number {orign} is divisible by 11.')
	else:print(f'The number {orign} is not divisible by 11.')