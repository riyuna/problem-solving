n=int(input())
if n%2==1:
	print(n//2+1, n//2)
elif n%4==0:
	print(n//4+1, n//4-1)
else:print("impossible")