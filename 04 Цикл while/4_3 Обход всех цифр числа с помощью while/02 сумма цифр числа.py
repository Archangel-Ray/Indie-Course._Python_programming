"""
Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа
"""
number = int(input())
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10
print(sum_of_digits)
