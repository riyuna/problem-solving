import sys
x,p=map(float,input().split())
x/=100
p/=100
if p==0:
    print(0)
    sys.exit()
q=(1-p)/p
d=dict()
d[0]=1
for i in range(20600):
    d[-i-1]=d[-i]/q
for i in range(2500):
    d[i+1]=d[i]*q
mx=0
for i in range(20600):
    for j in range(2500):
        if i==j==0:res=0
        else:res=(1-d[-i])/(d[j]-d[-i])
        mx=max(res*j-(1-x)*i*(1-res),mx)
print(mx)