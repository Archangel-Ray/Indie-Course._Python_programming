"""
Дано значение температуры в градусах Фаренгейта. Определить значение этой же температуры в градусах Цельсия.
    Температура по Цельсию C и температура по Фаренгейту F связаны следующим соотношением:
    C=((F−32)∗5)/9

Входные данные

    На вход программе поступает вещественное число F  - температура в градусах по Фаренгейту

Выходные данные

    Программа выводит градусы Цельсия
"""
print(((float(input()) - 32) * 5) / 9)
