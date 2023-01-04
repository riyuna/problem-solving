mod=10**9+7
n=int(input())
fact=1
for i in range(1, n+1):
	fact*=i
	fact%=mod

if n<4:
	if n==1:
		print(1)
		print(0)
		print(0)
	if n==2:
		print(2)
		print(1)
		print(0)
	if n==3:
		print(12)
		print(6)
		print(6)

else:
	res1=fact*pow(2, n*(n-1)//2-n+1, mod)
	res1%=mod
	res2=fact*(n+1)*pow(2, n*(n-1)//2-n-2, mod)
	res2%=mod
	res3=fact*n*pow(2, n*(n-1)//2-n-2, mod)
	res3%=mod
	print(res1)
	print(res2)
	print(res3)