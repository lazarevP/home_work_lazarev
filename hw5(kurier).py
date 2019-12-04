
print('enter the flat number') 
flat = int(input())
print('enter the number of floors per one porch')
floors = int(input())
print('enter the number of flats per one floor')
flats_per_floor = int(input())
porch = flat // (floors * flats_per_floor)
if flat % (floors * flats_per_floor):
	flat = flat - (porch * floors * flats_per_floor)
	floor = flat // flats_per_floor		
	if flat % flats_per_floor:
		print('Porch number', porch + 1, "Floor number is", floor + 1)
	else:
		print('Porch number', porch + 1, "Floor number is", floor)
else:
	flat = flat - ((porch - 1) * floors * flats_per_floor)
	floor = flat // flats_per_floor
	if flat % flats_per_floor:
		print('Porch number', porch, "floor number is", floor + 1)
	else:
		print('Porch number', porch, "floor number is", floor)
	

	

