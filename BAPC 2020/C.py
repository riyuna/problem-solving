n, p = map(int, input().split())

time_penalty_list = [int(input()) for _ in range(n)]

decr_no = 0

for i in range(n-1):
    if time_penalty_list[i] > time_penalty_list[i+1]:
        decr_no += 1

if decr_no < p:
    print("ambiguous")

else:
    for i in range(n-1):
        print(decr_no)
        if time_penalty_list[i] > time_penalty_list[i+1]:
            decr_no -= 1