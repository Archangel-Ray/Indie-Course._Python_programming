"""
В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько зарплата
самого высокооплачиваемого из них отличается от самого низкооплачиваемого.

Входные данные
Размеры зарплат всех сотрудников вводятся в одну строку через пробел. Каждая заработная плата – это натуральное число,
не превышающее 105. И гарантируется, что все зарплаты различны

Выходные данные
Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.

Примечание: функциями min и max, а также сортировками пользоваться нельзя, мы же условный оператор изучаем)
"""
salary_list = list(map(int, input().split()))
lesser = salary_list[0]
greater = 0
for salary in salary_list:
    if salary > greater:
        greater = salary
    if salary < lesser:
        lesser = salary
print(greater - lesser)
