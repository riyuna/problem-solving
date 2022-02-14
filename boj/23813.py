n=input()
length=len(n)
n=int(n)
orign=n
res=n
while True:
    newn=(n//10)+(n%10)*10**(length-1)
    if newn==orign:break
    res+=newn
    n=newn

print(res)