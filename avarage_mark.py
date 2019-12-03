my_class = {'Pasha': (5,1,3,4,1), 'Sasha': (2,2,3,4,5), 'Dasha': (5,2,3,5,5), 'Natasha': (4,2,3,4,5)}
list_of_avarage_marks = []
for name in my_class:
	avarage = sum(my_class[name])/len(my_class[name])
	my_class[name] = avarage
	print(name, 'has avarage mark', avarage)
	list_of_avarage_marks.append(avarage)
for name in my_class:
	if max(list_of_avarage_marks) == my_class[name]:
		print('the biggest avarage mark has', name, 'and it is', my_class[name])
	if min(list_of_avarage_marks) == my_class[name]:
		print('the lowest avarage mark has', name, 'and it is', my_class[name])



