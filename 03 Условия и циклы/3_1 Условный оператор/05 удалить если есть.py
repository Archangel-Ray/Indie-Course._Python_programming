"""
Программа получает на вход список из целых чисел, при этом гарантируется, что числа в списке повторяться не будут.
Ваша задача удалить из этого списка числа 3, 5, 7 и 9.

Обратите внимание, что каждое из чисел 3, 5, 7 и 9. необязательно должно присутствовать во введенном списке.

В качестве ответа необходимо распечатать измененный список

Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

a = list(map(int, input().split()))
"""
a = list(map(int, input().split()))
for number in [3, 5, 7, 9]:
    if number in a:
        a.remove(number)
print(a)
