from math import gcd
a,b=input().split('.')
n=int(a)*100+int(b)
k=gcd(n, 36000)
print(36000//k)