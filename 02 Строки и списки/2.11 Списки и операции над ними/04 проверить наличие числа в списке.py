"""
Программа получает на вход список из целых чисел. Ваша задача вывести True в случае, если в данном списке встречается
    значение 777. В противном случае вывести False

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной my_list вам необходимо написать строчку

my_list = list(map(int, input().split()))
"""
my_list = list(map(int, input().split()))
print(777 in my_list)
