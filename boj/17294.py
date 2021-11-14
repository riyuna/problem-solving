L=list(map(int, list(input())))
d=-15
state=True
for i in range(len(L)-1):
    if d==-15:d=L[i+1]-L[i]
    else:
        if L[i+1]-L[i]==d:continue
        else:
            state=False
            break
print(['흥칫뿡!! <(￣ ﹌ ￣)>','◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'][state])