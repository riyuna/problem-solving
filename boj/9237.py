n=int(input())
L=list(map(int,input().split()))
L.sort()
for i in range(n):
	L[i]+=(n-i)
print(max(L)+1)