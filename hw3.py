file = open("numbers.txt")
new_list = []
counter = 0
for line in file:
	line = list(map(int,line.split()))
	new_list.append(line)
for li in new_list:
	fizz = li[0]
	buzz = li[1]
	third_num = li[2] 
	counter += 1
	print('three numbers №', counter)
	for num in range(1,third_num + 1):
		if not num % fizz and not num % buzz:
			print("FB")
		elif not num % fizz:
			print("F")
		elif not num % buzz:
			print("B")
		else:
			print(num)
