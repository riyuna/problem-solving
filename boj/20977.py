n=int(input())
s=input()
ct=[0,0,0]
for i in s:
    if i=='J':ct[0]+=1
    if i=='O':ct[1]+=1
    if i=='I':ct[2]+=1
print('J'*ct[0]+'O'*ct[1]+'I'*ct[2])