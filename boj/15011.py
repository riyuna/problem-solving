a,b=map(int,input().split())
if a%2==0:print(0)
else:
	if b%2==1:print(1)
	elif a<b:print(2)
	else:print(0)