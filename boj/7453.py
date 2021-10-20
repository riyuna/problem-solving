n=int(input())
L1=[]
L2=[]
L3=[]
L4=[]
for i in ' '*n:
    a,b,c,d=map(int,input().split())
    L1.append(a)
    L2.append(b)
    L3.append(c)
    L4.append(d)
dic=dict()
for i in range(n):
    for j in range(n):
        k2=L3[i]+L4[j]
        if k2 in dic:dic[k2]+=1
        else:dic[k2]=1
ct=0
for i in range(n):
    for j in range(n):
        k=L1[i]+L2[j]
        if -k in dic:ct+=dic[-k]
print(ct)