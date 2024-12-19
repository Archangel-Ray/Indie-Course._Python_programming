"""
Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа
"""
number = int(input())
product_of_numbers = 1
while number > 0:
    product_of_numbers *= number % 10
    number //= 10
print(product_of_numbers)
