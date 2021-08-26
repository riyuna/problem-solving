def solve(L):
    x1,y1=L[0]
    x2,y2=L[1]
    x3,y3=L[2]
    x4,y4=L[3]
    xL=[x1,x2,x3,x4]
    yL=[y1,y2,y3,y4]
    minx=10**9
    for i in range(4):
        for j in range(i):
            xx1, xx2=xL[i],xL[j]
            M=[0,1,2,3]
            M.remove(i)
            M.remove(j)
            a,b=M
            nxL=xL[:]
            if abs(xx1-xL[a])+abs(xx2-xL[b])<abs(xx1-xL[b])+abs(xx2-xL[a]):
                dist = abs(xx1-xL[a])+abs(xx2-xL[b])
                d=abs(xx1-xx2)
                nxL[a]=xx1
                nxL[b]=xx2
                mind=10**9
                for k in range(4):
                    if k==a:
                        ydist1=abs(i-(a+d))
            else:
                dist = abs(xx1-xL[b])+abs(xx2-xL[a])
                nxL[a]=xx2
                nxL[b]=xx1
            

for i in ' '*int(input()):
    L=[]
    for j in ' '*4:
        L.append(list(map(int,input().split())))
    print(solve(L))