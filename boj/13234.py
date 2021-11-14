L=input().split()
res=True
if 'AND' in L:
    if 'false' in L:res=False
if 'OR' in L:
    if 'true' not in L:res=False
print(['false', 'true'][res])