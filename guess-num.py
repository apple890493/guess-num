import random
start = input("Please decide a starting number: ")
end = input("Please decide a ending number: ")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1 快寫
	print("")
	num = input("Enter number: ")
	num = int(num)
	if num == r:
		print("Bingo!")
		break
	elif num > r:
		print("Bigger than answer!")
	elif num < r:
		print("Smaller than answer!")
	print("This is count", count, "times!") #不用寫三次進去避免重複性!