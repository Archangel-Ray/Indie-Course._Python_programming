"""
Программа принимает на вход одно натуральное число и выводит на экран минимальную и максимальную цифры данного числа
в отдельных строчках
"""
number = int(input())
minimum_digit = maximum_digit = number % 10
number //= 10
while number > 0:
    last = number % 10
    if last < minimum_digit:
        minimum_digit = last
    elif last > maximum_digit:
        maximum_digit = last
    number //= 10
print(minimum_digit, maximum_digit, sep="\n")
