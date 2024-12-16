"""
Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду. Ваня хочет построить пирамиду
следующим образом: на верхушке пирамиды должен находиться 1 кубик, на втором уровне — 1+2=3 кубика,
на третьем — 1+2+3=6 кубиков, и так далее.
Таким образом, на i-м уровне пирамиды должно располагаться 1+2+...+(i-1)+i кубиков.

Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.

Входные данные
В первой строке записано целое число n (1≤n≤104) — количество кубиков, подаренных Ване.

Выходные данные.
Выведите единственной строкой максимально возможную высоту пирамиды.
"""
maximum_limit = int(input())
number = 0
sum_of_previous_numbers = 0
while maximum_limit > sum_of_previous_numbers + number:
    number += 1
    sum_of_previous_numbers += number
    maximum_limit -= sum_of_previous_numbers
print(number)
