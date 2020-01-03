num = int(input())
if num % 2 and not num % 3 and not num % 5 and num % 10 != 0:
	print("it is")
else:
	print("it is not")