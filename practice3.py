



import random

stud_dict = {}
students = ['vasya', 'kolya', 'petya', 'masha', 'platon']
for std in students:
	stud_dict[std] = []
	for _ in range(1,6):
		stud_dict[std].append(random.randint(1,5))
print(stud_dict)

# for name in stud_dict:
# 	print('student {name} has average mark {mark}'\
# 		.format(
# 			name = name,
# 			mark = sum(stud_dict.get(name))/len(stud_dict.get(name))))


# # # flats_per_floor = 8 
# # # floors = 24

# # # flat_needed = int(input())
# # # current_floor = 1
# # # while current_floor <= floors:
# # # 	if flat_needed <= current_floor * flats_per_floor:
# # # 		print('floor', current_floor, 'appartment found')
# # # 		break
# # # 	current_floor += 1




