from collections import deque
deq=deque([])
n=int(input())
L=list(map(int,input().split()))
for i in range(n):
    if len(deq)==0:
        deq.append((i+1, L[i]))
        print(0,end=' ')
    else:
        while len(deq) and deq[-1][1]<=L[i]:
            deq.pop()
        if len(deq)==0:print(0, end=' ')
        else:print(deq[-1][0], end=' ')
        deq.append((i+1, L[i]))
