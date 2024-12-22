"""
Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК).
"""
a, b = map(int, input().split())
product = a * b
while a:
    a, b = b % a, a
product = product // b
print(product)
