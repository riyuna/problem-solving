n=int(input())
k=sum(list(map(int,input().split())))
print(n*(n+1)//2-k)