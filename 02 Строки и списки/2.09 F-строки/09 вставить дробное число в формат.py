"""
Средний курс валют за три дня
Напишите, программу, которая рассчитывает средний курс валюты за последние три дня.

Входные данные
Три вещественных числа (курс валюты за три дня) в отдельных строках.

Выходные данные
Программа находит средний курс валюты за последние три дня и выводит текст в формате:

Средний курс доллара за последние три дня: <средний курс> RUB.

где результат среднего курса округлен с точностью до двух знаков после запятой.
"""
first, second, third = float(input()), float(input()), float(input())
print("Средний курс доллара за последние три дня: %.2f RUB." % ((first + second + third) / 3))
