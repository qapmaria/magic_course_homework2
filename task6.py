# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
a = max(new_lst)
b = min(new_lst)
c = a - b
print(c)
