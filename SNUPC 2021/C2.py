n=int(input())
L=[]
for i in ' '*n:L.append(tuple(sorted(map(int,input().split()))))
if n==10:print(-1)
else:
    if (1,4) in L and (2,5) in L and (1,3) in L and (3,5) in L and (2,4) in L:print(2)
    elif ((1,4) in L and (2,5) in L) or ((1,4) in L and (3,5) in L) or ((2,4) in L and (3,5) in L) or ((1,3) in L and (2,4) in L) or ((1,3) in L and (2,5) in L):
        print(1)
    else:print(0)