import random

start = input('Enter a start number: ')
end = input('Enter a end number: ')

start = int(start)
end = int(end)

r = random.randint(start,end)

count = 0

while True:

	count += 1 # count = count + 1
	
	num = input('Make a guess:')
	if num == '':
		print('You must input something')
	else:
		num = int(num)
		if r == num:
			print('You are correct!')
			print('This is your', count, 'attempt')
			break
		elif num > r:
			print('bigger than r')
		elif num < r:
			print('smaller than r')
		print('This is your', count, 'attempt')