n=int(input())
s=input()
A=[0]*n
B=[0]*n
C=[0]*n
a=s.count("A")
b=s.count('B')
c=s.count('C')
for i in range(n):
    if i==0:
        A[i]=a-s[:a].count('A')
        B[i]=b-s[:b].count('B')
        C[i]=c-s[:c].count('C')
    else:
        A[i]=A[i-1]
        B[i]=B[i-1]
        C[i]=C[i-1]
        if s[i-1]=='A':A[i]+=1
        if s[i-1]=='B':B[i]+=1
        if s[i-1]=='C':C[i]+=1
        if s[(i+a-1)%n]=='A':A[i]-=1
        if s[(i+b-1)%n]=='B':B[i]-=1
        if s[(i+c-1)%n]=='C':C[i]-=1

mn = n
for i in range(n):
    k1=A[i]+B[(i+a)%n]+C[(i+a+b)%n]
    k2=A[i]+C[(i+a)%n]+B[(i+a+c)%n]
    mn=min(min(k1,k2),mn)

print(mn)