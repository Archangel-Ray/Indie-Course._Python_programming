"""
Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.
"""
number = int(input())
while number > 0:
    print(number % 10)
    number //= 10
