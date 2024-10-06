n=int(input())
score=0
L=list(map(int,input().split()))
score+=L[0]
for i in range(1, n):
	if L[i-1]+1!=L[i]:score+=L[i]
print(score)