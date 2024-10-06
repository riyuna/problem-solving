n=int(input())
L=list(map(int,input().split()))
check=dict()
check[0]=True
m=int(input())
for i in range(n):
	k=L[i]
	new=set()
	for j in check:
		new.add(j+k)
		new.add(j-k)
	for j in new:check[j]=True
# print(check)
for i in list(map(int,input().split())):
	print('NY'[i in check],end=' ')