import sys
input=sys.stdin.readline
print=sys.stdout.write
L=[]
for i in ' '*int(input()):L.append(int(input()))
L.sort()
for i in L:print(str(i)+'\n')