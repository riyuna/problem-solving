import bisect
L=[1, 4, 6, 7, 9, 11]
for i in range(15):
    print(bisect.bisect_right(L, i))