"""
Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

a = list(map(int, input().split()))
"""
a = list(map(int, input().split()))
print(a.count(999))
