n=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)
tot = sum(L)
ct = 0
d = tot//n
r = tot%n
for i in range(n):
	if i<r:ct+=abs(L[i]-d-1)
	else:ct+=abs(L[i]-d)
print(ct//2)