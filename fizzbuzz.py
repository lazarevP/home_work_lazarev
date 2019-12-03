fizz = int(input())
buzz = int(input())
third_num = int(input())
for num in range(1,third_num + 1):
	if not num % fizz and not num % buzz:
		print("FB")
	elif not num % fizz:
		print("F")
	elif not num % buzz:
		print("B")
	else:
		print(num)		