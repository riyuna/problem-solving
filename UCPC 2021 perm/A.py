def check(s, a):
    ct = 0
    while ct<len(s):
        aa = str(a)
        if s[ct:ct+len(aa)] != aa:return False
        a+=1
        ct+=len(aa)
    return a-1

s=input()
if len(s)==1: print(int(s), int(s))
elif len(s)==2:
    if int(s[0])+1==int(s[1]):print(int(s[0]), int(s[1]))
    else:print(int(s), int(s))
else:
    a1 = int(s[0])
    a2 = int(s[:2])
    a3 = int(s[:3])
    b1 = check(s, a1)
    b2 = check(s, a2)
    b3 = check(s, a3)
    if b1: print(a1, b1)
    elif b2: print(a2, b2)
    else: print(a3, b3)