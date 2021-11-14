s=input()
ctL=[0]*26
for i in s:
    if i==' ':continue
    ctL[ord(i)-65]=1
L=ctL+ctL
seg1=0
seg2=0
ct=0
while ct<sum(ctL):
    ct+=L[seg2]
    seg2+=1
while L[seg1]==0:seg1+=1
def solve(seg1, seg2):
    left=False
    dist=min(abs(seg1-26),abs(seg2-26))
    if abs(seg1-26)<abs(seg2-26):left=True
    return (dist+seg2-seg1,left)
mi=10**9
store1=0
stoer2=0
lstore=False
while seg2<52:
    k,left=solve(seg1,seg2)
    if mi>k:
        mi=k
        store1=seg1
        store2=seg2
        lstore=left
    seg2+=1
    if seg2>=52:break
    while seg2<52 and L[seg2]==0:seg2+=1
    seg1+=1
    while seg1<52 and L[seg1]==0:seg1+=1
print(mi+sum(ctL))
if lstore:
    for i in range(store1, store2+1):
        if ctL[i%26]:print(chr(i%26+65),end='')
else:
    for i in range(store2,store1-1,-1):
        if ctL[i%26]:print(chr(i%26+65),end='')