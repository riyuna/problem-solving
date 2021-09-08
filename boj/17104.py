import math
def fft(L, w):
    n=len(L)
    if n==1:return
    even=[0]*(n//2)
    odd=[0]*(n//2)
    for i in range(n):
        if i%2:odd[i//2]=L[i]
        else:even[i//2]=L[i]
    fft(even, w**2)
    fft(odd, w**2)
    wp=1
    for i in range(n//2):
        L[i]=even[i]+odd[i]*wp
        L[i+n//2]=even[i]-odd[i]*wp
        wp*=w
def multiply(L1,L2):
    n=2
    while n<len(L1) or n<len(L2):n*=2
    n*=2
    L1+=[0]*(n-len(L1))
    L2+=[0]*(n-len(L2))
    w=complex(math.cos(2*math.pi/n),math.sin(2*math.pi/n))
    fft(L1,w)
    fft(L2,w)
    L=[0]*n
    for i in range(n):L[i]=L1[i]*L2[i]
    fft(L,1/w)
    for i in range(n):
        L[i]/=n
        L[i]=complex(round(L[i].real), round(L[i].imag))
    return L
    
# t=int(input().split())

L=[1]*(11)
L[0]=0
L[1]=0
ct=1
while ct<10:
    ct+=1
    if L[ct]==0:continue
    for j in range(ct*2, 10, ct):L[j]=0
L1=L[:]
L2=L
res=multiply(L1, L2)
print(res)