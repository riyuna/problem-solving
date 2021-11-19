from collections import deque
s=input()
t=input()
c=len(t)
a=deque([])
for i in s:
    a.append(i)
    if i==t[-1]:
        check=True
        if len(a)<c:check=False
        else:
            for i in range(c):
                if a[-1-i]!=t[-1-i]:
                    check=False
                    break
        if check:
            for _ in range(c):a.pop()
if len(a)==0:print('FRULA')
else:print(''.join(a))