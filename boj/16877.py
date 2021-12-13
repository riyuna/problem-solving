grun=[0,1,2,3]
fib=[1,2]
k=0
while k<(3*10**6):
    fib.append(fib[-1]+fib[-2])
    k=fib[-1]
pt=0
for i in range(4, 3*10**6+1):
    while fib[pt]<=i:pt+=1
    mem=dict()
    for j in range(pt):
        mem[grun[i-fib[j]]]=True
    res=0
    while res in mem:res+=1
    grun.append(res)
n=int(input())
res=0
for i in list(map(int,input().split())):
    res^=grun[i]
print('koosaga' if res else 'cubelover')