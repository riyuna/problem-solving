ct=0
for _ in ' '*int(input()):
    n=int(input())
    ct+=pow(n//10, n%10)
print(ct)