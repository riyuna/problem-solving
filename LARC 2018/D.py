users = dict()

for _ in range(int(input())):
	username, provider = input().split("@")
	username = username.split("+")[0].replace(".", "")

	if provider in users:
		users[provider].add(username)
	else:
		users[provider] = set([username])

tot_user_no = 0
for provider in users.keys():
	tot_user_no += len(users[provider])

print(tot_user_no)
