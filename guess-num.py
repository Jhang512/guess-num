import random

r = random.randint(1,100)

while True:
	num = input('Make a guess:')
	num = int(num)
	if r == num:
		print('You are correct!')
		break
	else if num > r:
		print('bigger than r')
	else if num < r:
		print('smaller than r')