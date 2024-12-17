"""
В вашем распоряжении имеется два отсортированных списка по неубыванию элементов, состоящих из n и m элементов

Ваша задача слить их в один отсортированный список размером n + m

Входные данные
Программа получает на вход два числа n и m - количество элементов первого списка и второго списков

Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка

Выходные данные.
Слить два списка в один в порядке неубывания и вывести элементы полученного списка

P.S.: пользоваться встроенной сортировкой запрещено

Примечание: для вывода результирующего списка вы можете использовать следующую конструкцию

print(*result) # где result - итоговый список
"""
n, m = map(int, input().split())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
new_list = list()
while first_list or second_list:
    if first_list:
        if second_list:
            if first_list[0] < second_list[0]:
                new_list.append(first_list.pop(0))
            else:
                new_list.append(second_list.pop(0))
        else:
            new_list.extend(first_list)
            first_list.clear()
    else:
        new_list.extend(second_list)
        second_list.clear()
print(*new_list)
