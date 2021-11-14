fib=[1,1]
for i in range(40):
    fib.append(fib[-1]+fib[-2])
d,k=map(int,input().split())
a=0
while True:
    a+=1
    if (k-a*fib[d-3])%fib[d-2]==0:
        b=(k-a*fib[d-3])//fib[d-2]
        print(a)
        print(b)
        break