for j in range(int(input())):
    n=int(input())
    ct=0
    s1=input()
    s2=input()
    for i in range(n):
        if s1[i]!=s2[i]:ct+=1
    print(f"Case {j+1}: {ct}")