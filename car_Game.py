command = ""
started = False

while True:
	command = input("> ").lower()
	if command == "start":
		print("Car has started...")
		if started:
			print("Car already started!")
		else:
			started = True
			print("Car started...")
	elif command == "stop":
		print("Car has been stopped...")
		if not started:
			print("Car has already been stopped...")
		else:
			started = False
			print("Car stopped")

	elif command == "help":
		print("""
start - to start the car
stop - to stop the car
quit - to exit
			""")

	elif command == "quit":
		break
	else:
		print("Sorry I don't understand that...")