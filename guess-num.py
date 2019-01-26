import random
r = random.randint(1, 100)

while True:
	num = input("Enter number: ")
	num = int(num)
	if num == r:
		print("Bingo!")
		break
	elif num > r:
		print("Bigger than answer!")
	elif num < r:
		print("Smaller than answer!")



