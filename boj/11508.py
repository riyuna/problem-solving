import sys
input=sys.stdin.readline
L=[]
for i in ' '*int(input()):L.append(int(input()))
L.sort()
L=L[::-1]
res=0
for i in range(len(L)):
	if i%3!=2:res+=L[i]
print(res)