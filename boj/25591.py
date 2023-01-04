a,b=map(int,input().split())
k=(100-a)*(100-b)
print(100-a, 100-b, 100-(a+b), k, k//100, k%100)
print(a*b//100, a*b%100)