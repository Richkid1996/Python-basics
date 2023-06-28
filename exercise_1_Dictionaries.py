phone = input("Phone: ")
number = {"1": "One", "2": "Two", "3": "Three", "4": "Four"}
output = ""
for character in phone:
	output += number.get(character,"!") + " "
print(output)
