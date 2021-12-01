n=int(input())
a0=int(input())
res=0
for i in ' '*n:
    a=int(input())
    res+=min((a0-a)%360, (a-a0)%360)
    a0=a
print(res)