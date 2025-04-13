#3. Використати вивчені функції Python:
print ("--- Робота з рядками ---")

print ("\n1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()")
num_str = 125
num_str = str(num_str)
print("num_str : ", num_str, "Тип : ", type(num_str))

print ("\n2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'.")
message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print("message після заміни : ", message)

print ("\n3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join")
split_test = 'This is a split test'
split_result = split_test.split()
print("split_result : ", split_result)
string_join = ' '.join(split_result)
print("string_join : ", string_join)

print ("\n4. Визначити довжину рядку string_join за допомогою функції len()")
length = len(string_join)
print("Довжина string_join : ", length)


print ("\n\n--- Робота зі списками ---")
print ("\n 1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5")
list_append = [1, 2, 3]
list_append.append (4)
list_append.append (5)
print ("Оновлений список : ", list_append)

print ("\n 2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()")
list_extend = [4, 5, 6]
list_extend_1 = (7, 8, 9)
list_extend.extend (list_extend_1)
print ("Оновлений список : ", list_extend)

print ("\n 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()")
index = list_extend.index (6)
print ("Індекс елемента 6 у списку list_extend  : ", index)

print ("\n 4. Визначити довжину списку list_append за допомогою функції len()")
print ("Довжина списку list_append  : ", len(list_append))


print ("\n\n--- Робота зі словниками ---")
print ("\n 1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where")
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print("Значення ключа car :", dict_test['car'])
print("Значення ключа where :", dict_test['where'])

print ("\n 2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення")
print("Ключі:", dict_test.keys())
print("Значення:", dict_test.values())

print ("\n 3. За допомогою функції items() вивести на екран пари ключ - значення")
print("\nПари ключ-значення:", dict_test.items())


