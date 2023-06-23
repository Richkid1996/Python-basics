usernames = ["Richkid", "Josh", "Admin", "Rpbert", "Kevin"]

for username in usernames:
	if username == 'Admin':
		print("\nHello Admin, would you like to see a status report?")
	else:
		print(f"\nHello {username}, thank you for logging in again")