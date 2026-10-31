from random import randint

player = input("Select: Dam|La|Keo\n")

computer = randint(0,2)
if  player == "Dam" or player == "La" or player == "Keo":
	if computer == 0:
		computer = str("Dam")
	if computer == 1:
		computer = str("La")
	if computer == 2:
		computer = str("Keo")
	print(computer)
	if player == computer:
		print("draw")

	if player == "Dam":
		if computer == "Keo":
			print("Win")
		if computer == "La":
			print("Lose")

	if player == "La":
		if computer == "Dam":
			print("Win")
		if computer == "Keo":
			print("Lose")

	if player == "Keo":
		if computer == "La":
			print("Win")
		if computer == "Dam":
			print("Lose")
else:
	print("Ban da nhap sai")

