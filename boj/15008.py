n=int(input())
L=list(map(int,input().split()))
L.sort()
pt=n-1
ct=0
a=0
b=0
while True:
	ct+=1
	if ct%2:a+=L[pt]
	else:b+=L[pt]
	if pt==0:break
	pt-=1
print(a,b)