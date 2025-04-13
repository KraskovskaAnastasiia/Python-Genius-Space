#2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
num1, num2 = 10, 20
float1, float2 = 3.14, 2.71
str1, str2 = "apple", "banana"
bool1, bool2 = True, False
list1, list2 = [1, 2, 3], [1, 2, 4]
dict1, dict2 = {"a": 1}, {"a": 1, "b": 2}
tuple1, tuple2 = (1, 2), (1, 3)

print("\nЧисла : ", num1,", ", num2)
print("Дробові числа : ", float1, ", ",float2)
print("--- Порівняння чисел ---")
print("num1 < num2 : ", num1 < num2)
print("float1 >= float2 : ", float1 >= float2)
print("num1 == float2 : ", num1 == float2)

print("\nРядки : ", str1,", " ,str2)
print("--- Порівняння рядків ---")
print("str1 == str2 : ", str1 == str2)
print("str1 < str2 : ", str1 < str2)
print("str1 != apple", str1 != "apple")

print("\nБулеві значення : ", bool1,", ", bool2)
print("--- Порівняння булевих значень ---")
print("bool1 == bool2 : ", bool1 == bool2)
print("bool1 and bool2 : ",bool1 and bool2)
print("bool1 or not bool2 : ",bool1 or not bool2)

print("\nСписки : ", list1,", ", list2)
print("--- Списки ---")
print("list1 == list2 : ",list1 == list2)
print("list1 < list2 : ",list1 < list2)
print("len(list1) == len(list2) : ",len(list1) == len(list2))

print("\nСловники : ", dict1,", ", dict2)
print("--- Словники ---")
print("dict1 == dict2 : ",dict1 == dict2)
print("len(dict1) < len(dict2) : ",len(dict1) < len(dict2))

print("\nКортежі : ", tuple1,", ", tuple2)
print("--- Кортежі ---")
print("tuple1 == tuple2 : ",tuple1 == tuple2)
print("tuple1 < tuple2 : ",tuple1 < tuple2)
print("len(tuple1) == len(tuple2) : ",len(tuple1) == len(tuple2))
