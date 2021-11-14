prime=[True]*(10001)
pL=[]
prime[0]=False
prime[1]=False
for i in range(2, 10001):
    if not prime[i]:continue
    for j in range(i*2, 10001, i):
        prime[j]=False
    pL.append(i)
def isPrime(n):
    if n<2:return False
    if n<10000 and prime[n]:return True
    for p in pL:
        if n%p==0:return False
    return True
res=[[]for i in range(8)]
res[0]=[2,3,5,7]
for i in range(1, 8):
    for j in res[i-1]:
        for k in range(1, 10, 2):
            if isPrime(j*10+k):res[i].append(j*10+k)
for i in res[int(input())-1]:
    print(i)