while True:
    s=input()
    if s=='#':break
    s=s.lower()
    k=s.split()[0]
    ct=-1
    for i in s:
        if i==k:ct+=1
    print(k, ct)