from _collections import OrderedDict


table_of_sizes = OrderedDict({
"обхват талии, см": ('63-65','66-69', '70-74', '75-78','79-83', '84-89', '90-94', '95-97'),
"обхват бедер, см": ('89-92', '93-96', '97-101', '102-104', '105-108', '109-112', '113-117', '118-122'), 
"международный": ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'),
"Россия": (42, 44, 46, 48, 50, 52, 54, 56),
"Германия": (36, 38, 40, 42, 44, 46, 48, 50),
"США": (8, 10, 12, 14, 16, 18, 20), 
"Франция": (38, 40, 42, 44, 46, 48, 50, 52),
"Великобритания":(24, 26, 28, 30, 32, 34, 36, 38)})

list_of_keys = []

for key in table_of_sizes:
    list_of_keys.append(key)

text1 = 'enter the number of country u want to change the size:\n0 - {0};\n1 - {1};\n2 - {2};\n3 - {3};\n4 - {4};\n5 - {5};\n6 - {6};\n7 - {7}\n'.format(*list_of_keys)

country_from = int(input(text1))
country_from = list_of_keys[country_from]

text2 = 'enter the number of country u want to get the size:\n0 - {0};\n1 - {1};\n2 - {2};\n3 - {3};\n4 - {4};\n5 - {5};\n6 - {6};\n7 - {7}\n'.format(*list_of_keys)

country_to = int(input(text2))
country_to = list_of_keys[country_to]

print('choose the size u want to change and enter the number near it')

n = 0
for i in table_of_sizes[country_from]:
    print(i, ' - {}'.format(n))
    n += 1
index_of_size1 = int(input())

print('the size of {} is {}'.format(country_to, table_of_sizes[country_to][index_of_size1]))


