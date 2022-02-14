n=int(input())
L=list(map(int,input().split()))
L.sort()
mid=L[n//2] if n%2 else L[n//2-1]
mean=sum(L)/n+0.5
if int(mean)==mean:mean=int(mean)-1
else:mean=int(mean)
print(mid, mean)