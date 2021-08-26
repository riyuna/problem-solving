mod = 998244353
n=int(input())
s=input()
L=list(map(int,input().split()))
def rev(n):
    return pow(n, mod-2, mod)
split_L=[(0, 0, 0, 0), (0, 0, 0, 0)]
ct=0
score=0
n_fact = 1
b=0
for i in s:
    if i=='B':b+=1
for i in range(n):
    n_fact*=(i+1)
    n_fact%=mod
    if i==0 or s[i-1]==s[i]:
        ct+=1
        score+=L[i]
    else:
        split_L.append((ct, score, i, split_L[-2][3]+ct, 'B' if s[i]=='W' else 'W'))
        ct=1
        score=L[i]


split_L.append((ct, score, i+1, split_L[-2][3]+ct, s[i]))
res=0
split_L=split_L[2:]

for i in range(len(split_L)):
    if i==0 or i==len(split_L)-1:continue
    perm = rev(split_L[i][0])
    front = split_L[i-1][2]
    back = n-split_L[i][2]
    front_sel = split_L[i][2] - split_L[i][3]
    back_sel = b-split_L[i][0]-front_sel if split_L[i][4] == 'B' else (n-b)-split_L[i][0]-front_sel

    perm*=front_sel
    perm*=back_sel
    perm*=rev(front)
    perm*=rev(back)
    perm%=mod
    res+=perm
    res%=mod

res*=n_fact
res%=mod

print(res)