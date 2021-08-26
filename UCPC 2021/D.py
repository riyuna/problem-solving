import sys


input = sys.stdin.readline


def get_swallow():
    x, y, v = map(int, input().split())
    return (x, y, v)


n = int(input())
swallows_x = [get_swallow() for _ in range(n)]
swallows_y = swallows_x[:]

swallows_x.sort(key=lambda x: x[0])
swallows_y.sort(key=lambda x: x[1])

exclude_x = []
exclude_y = []
chosen_line = 0
total_point_sum = 0


while chosen_line != 3:
    current_max_sum = 0
    is_x = True
    coor = 0
    
    current_x = -1
    current_sum = 0
    for (x, y, v) in swallows_x:
        if x in exclude_x:
            continue
        if y in exclude_y:
            continue
        if current_x != x:
            if current_max_sum < current_sum:
                current_max_sum = current_sum
                coor = current_x
            current_x = x
            current_sum = v
        else:
            current_sum += v
    
    if current_max_sum < current_sum:
        current_max_sum = current_sum
        coor = current_x
    
    current_y = -1
    current_sum = 0
    for (x, y, v) in swallows_y:
        if x in exclude_x:
            continue
        if y in exclude_y:
            continue
        if current_y != y:
            if current_max_sum < current_sum:
                current_max_sum = current_sum
                is_x = False
                coor = current_y
            current_y = y
            current_sum = v
        else:
            current_sum += v
    
    if current_max_sum < current_sum:
        current_max_sum = current_sum
        is_x = False
        coor = current_y
    
    total_point_sum += current_max_sum
    if is_x:
        exclude_x.append(coor)
    else:
        exclude_y.append(coor)
    
    chosen_line += 1

print(total_point_sum)