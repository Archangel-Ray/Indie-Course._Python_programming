"""
Программа определяет наименование месяца по его номеру n. Название месяца пишется с заглавной буквы

Программа получает на вход номер месяца - натуральное число N (N<=12)
и в зависимости от его значения вывод название месяца
"""
import calendar
import locale
# import pymorphy2

# morph = pymorphy2.MorphAnalyzer()
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
n = int(input())

if 0 < n <= 12:
    month = calendar.month_name[n]
    # month = morph.parse(month)[0].normal_form
    print(month.capitalize())
