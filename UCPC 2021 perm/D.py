n = int(input())
string = input()
L_num = list(map(int, input().split(' ')))
L = []

color = string[0]
biggest = 0
for i in range(n):
    if string[i] == color:
        biggest = max(biggest, L_num[i])
    else:
        L.append(biggest)
        biggest = L_num[i]
        color = string[i]
L.append(biggest)

def f(L):
    if len(L)==1:
        return 0
    if len(L)==2:
        return 0
    if len(L)==3:
        return L[1]
    L.pop(len(L)-1)
    L.pop(0)
    L.sort()
    L.reverse()
    sum=0
    for i in range((len(L)+1)//2):
        sum += L[i]
    return sum

print(f(L))