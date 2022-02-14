n=int(input())
L=list(map(int,input().split()))
print(sum(L)-min(L)+max(L))