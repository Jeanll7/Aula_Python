import sys
sys.stdout.reconfigure(encoding='utf-8')

list = ["chicago", "queens", "salvador", "pernambuco"]
print(list)

list2 = [2, 3, 5, 6, 8, 10]
print(list2)

list3 = [2.0, 3.5, 4.2]
print(list3)

list4 = [True, False]
print(list4)

# index        0        1       2     3    4
mixed_list = [True, "chicago", 2.5, False, 4]
print(mixed_list)

print(type(mixed_list))

print(mixed_list[1]) # = chicago

