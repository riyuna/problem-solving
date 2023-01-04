n,i,k=map(int,input().split())
mem = [pow(i/n, k) for i in range(n+1)]
res=0
for j in range(n):
	p_i = mem[j+1]-mem[j]
	if j+1<i: res+=i*p_i
	else: res+=p_i*(2+j)/2
print(res)