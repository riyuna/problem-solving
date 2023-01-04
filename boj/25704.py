n=int(input())
k=int(input())
res=k
if n>4:res=min(res, k-500)
if n>9:res=min(res, k*9//10)
if n>14:res=min(res, k-2000)
if n>19:res=min(res, k*3//4)

print(max(res,0))