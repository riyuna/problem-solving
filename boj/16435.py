n,l=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
for i in L:
	if i>l:break
	l+=1
print(l)