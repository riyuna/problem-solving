n=int(input())
ct=0
for i in range(1, n+1):
    ct+=str(i).count('3')+str(i).count('6')+str(i).count('9')
print(ct)