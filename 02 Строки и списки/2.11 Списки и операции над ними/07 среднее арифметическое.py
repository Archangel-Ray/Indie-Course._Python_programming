"""
Программа получает на вход список из целых чисел. Ваша задача найти среднее арифметическое введенного списка чисел

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной list_numbers
вам необходимо написать строчку

list_numbers = list(map(int, input().split()))
"""
list_numbers = list(map(int, input().split()))
print(sum(list_numbers)/len(list_numbers))
