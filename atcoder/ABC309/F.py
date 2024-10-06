import sys
input=sys.stdin.readline
L=[]
for i in ' '*int(input()):
    a,b,c=sorted(list(map(int,input().split())))
    L.append([a,b,c])

L.sort()
