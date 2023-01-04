n=int(input())
check=[0]*(n+1)
L=list(map(int,input().split()))
for i in range(n):L[i]-=1
mod=10**9+7

fact=[1]
for i in range(n):
	fact.append(fact[-1]*(i+1)%mod)

visit=[False]*n

for i in range(n):
	if not visit[i]:
		ct=0
		while not visit[i]:
			visit[i]=True
			ct+=1
			i=L[i]
		check[ct]+=1


res=1
for i in range(1, n+1):
	res*=(fact[check[i]]*pow(i, check[i], mod))
	res%=mod

flag=False
for i in range(1, n+1):
	if (i%2==0 and check[i]) or check[i]>1:flag=True

if flag:
	res= res//2 if res%2==0 else (res+mod)//2

print(res)