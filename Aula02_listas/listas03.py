import sys
sys.stdout.reconfigure(encoding='utf-8')

# index         0       1       2     3    4   5
mixed_list = [True, "chicago", 2.5, False, 4,  8]
# print(mixed_list)
print(type(mixed_list)) # = 'list'
print(mixed_list[-5]) # = ["chicago"] 
print(mixed_list[::]) # = :começo :fim => imprime toda a lista 
print(mixed_list[1:]) # = ["chicago", 2.5, False, 4, 8]
print(mixed_list[2:]) # = [2.5, False, 4, 8] 
print(mixed_list[:3]) # = [True, 'chicago', 2.5] 
print(mixed_list[:4]) # = [True, 'chicago', 2.5, False] 
print(mixed_list[1:4]) # = ["chicago", 2.5, False, 4] 
print(mixed_list[1:5:2]) # = acrescentar de 2 em 2





