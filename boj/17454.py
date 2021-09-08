import sys
input = sys.stdin.readline
for i in ' '*int(input()):
    a,b,c,d,e,f=map(int,input().split())
    if c>d or e>f:print('GOD')
    elif (d-c)*(f-e)<c*e:print('GOD')
    else:print('KDH')