text = "enter the odd number and observe the magic "
num = int(input(text))
text2 = 'enter the symbol u want to be shown as brilliant '
symbol = input(text2)
# while not num % 2:
# 	print("i told u to enter the odd number, not even")
# 	num = int(input())
if num % 2:
	spases = num //2
	stars = 1
	while stars <= num:
		print(' ' * spases, symbol * stars)
		spases -= 1
		stars += 2
	spases = 1
	stars = num - 2 
	while stars >= 1:
		print(" " * spases, symbol * stars)
		spases += 1
		stars -= 2	




