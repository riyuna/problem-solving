n=int(input())
L=list(map(int,input().split()))
L.sort()
q_index=n
for i in range(n):
	if L[i]<n-i:
		q_index-=1
	else:break
print(q_index)