n=int(input())
ladder=[]
for i in range(n-1):
    L=list(map(int,input().split()))
    L.pop(-1)
    ladder.append(L)

