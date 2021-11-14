def check(n):
    s=0
    nn=n
    while n:
        s+=n%10
        n//=10
    if nn%s==0:return True
    return False
ct=0
for i in range(1, int(input())+1):
    if check(i):ct+=1
print(ct)