def ct(n):
    res=0
    for i in range(1, n+1):
        if n%i==0:res+=1
    return res
for i in ' '*(int(input())):
    n=int(input())
    print(n, ct(n))