L=[]
for i in range(12):
	L.extend([i]*(i+1))

n=int(input())
M=list(map(int,input().split()))
res=0
for i in M:
	res^=L[i]
print('koosaga' if res else 'cubelover')