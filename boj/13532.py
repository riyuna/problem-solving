from math import log10
n=int(input())
lg2= log10(2)
if n%2:n-=1
print(int(n*lg2))