s=input()
count0=0
count1=0
s1=''
c0=0
c1=1
for i in s:
    if i=='1':c1+=1
    else:c0+=1
for i in s:
    if i=='1':
        count1+=1
        if count1*2>c1:s1+=i
    else:
        count0+=1
        if count0*2<=c0:s1+=i
print(s1)