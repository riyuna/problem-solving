n=int(input())
ct=0
for i in range(1, n):
    for j in range(i, n):
        if (n-i-j)<j:break
        if (n-i-j)<(i+j):ct+=1
print(ct)