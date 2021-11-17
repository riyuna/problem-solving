L=[True]*(10**6+1)
pdict=dict()
L[0]=False
L[1]=False
for i in range(2, 10**6+1):
    if L[i]==False:continue
    pdict[i]=True
    for j in range(i*2, 10**6+1, i):
        L[j]=False


def isPrime(n):
    global pdict
    return n in pdict

def isSquare(n):
    if n<0:return False
    return int(n**0.5)**2==n

def P2(A):
    n = len(A)
    ct=0
    for i in range(n):
        if isPrime(i) and isSquare(A[i]):ct+=A[i]
    return ct

############### SUBMIT THE CODE ABOVE ONLY ###############

print(P2([0, 100, 20, 100, 40])) # 100
print(P2([1,2,4,9,10,11]))
print(P2([1]))