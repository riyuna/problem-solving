import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))

S=0
for i in range(n):
    S+=(L[i][0]*L[(i+1)%n][1]-L[i][1]*L[(i+1)%n][0])
S=abs(S)/2

A=0
B=0
C=0
for i in range(n):
    A+=(L[i][0]*L[(i+1)%n][1]-L[(i+1)%n][0]*L[i][1])*(L[i][0]**2+L[i][0]*L[(i+1)%n][0]+L[(i+1)%n][0]**2+L[i][1]**2+L[i][1]*L[(i+1)%n][1]+L[(i+1)%n][1]**2)
    B+=(L[(i+1)%n][1]-L[i][1])*(L[(i+1)%n][0]**2+L[i][0]*L[(i+1)%n][0]+L[i][0]**2)
    C-=(L[(i+1)%n][0]-L[i][0])*(L[(i+1)%n][1]**2+L[i][1]*L[(i+1)%n][1]+L[i][1]**2)

A/=12
B/=6
C/=6

res=(2*A*S-2*B**2-2*C**2)/(S**2)
print(res)