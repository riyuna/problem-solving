s=input()
L=[1,0,0]
for i in s:
    if i=='A':L[0],L[1]=L[1],L[0]
    if i=='B':L[1],L[2]=L[2],L[1]
    if i=='C':L[0],L[2]=L[2],L[0]
if L[0]:print(1)
if L[1]:print(2)
if L[2]:print(3)