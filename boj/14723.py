n=int(input())
for i in range(1, 100):
    if (i-1)*(i-2)//2<n<=i*(i-1)//2:break
k=(i*(i-1))//2-n
print(k+1, i-k-1)