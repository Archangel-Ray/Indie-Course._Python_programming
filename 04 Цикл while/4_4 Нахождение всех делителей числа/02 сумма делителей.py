"""
Программа получает на вход натуральное число N.

Нужно найти сумму его делителей.
"""
n = int(input())
i = 1
natural_divisors = list()
while i * i <= n:
    if n % i == 0:
        natural_divisors.append(i)
        if i != n // i:
            natural_divisors.append(n // i)
    i += 1
print(sum(natural_divisors))
