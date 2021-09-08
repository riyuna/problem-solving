import sys
input = sys.stdin.readline

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)

def solve(L, start, end):
    n=end-start
    if n<2:return 0
    if n==2:return dist(L[start],L[start+1])
    if n==3:return min([dist(L[start],L[start+1]), dist(L[start+1], L[start+2]), dist(L[start], L[start+2])])

    sep = (L[start+n//2][0]+L[start+n//2-1][0])//2
    d = min(solve(L,start, start+n//2), solve(L, start+n//2, end))

    M=set()

    for i in range(n):
        d1 = sep-L[start+i][0]
        if d1**2<d:M.add((L[start+i][1], L[start+i][0]))

    M=list(M)
    M=sorted(M)

    for i in range(len(M)):
        for j in range(i+1, len(M)):
            if (M[i][1]-M[j][1])**2>d:break
            d = min(d, dist(M[i],M[j]))
    
    return d

L=[]

# with open("2.in.txt", 'r') as f:
#     lines = f.readlines()
#     for i in lines[1:]:
#         L.append(list(map(int,i.split())))




for i in ' '*int(input()):
    L.append(list(map(int,input().split())))
L.sort()
print(solve(L, 0, len(L)))